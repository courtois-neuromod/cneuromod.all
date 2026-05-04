import json
import re
import yaml
from pathlib import Path

from .constants import _CONTRIB_EMOJI, _CONTRIB_LABEL, _STATUS_ICON


def _render_citation(cff_path):
    with open(cff_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    ref = data.get('preferred-citation')
    if not ref:
        return ''

    authors = ref.get('authors', [])
    if len(authors) > 5:
        author_str = ', '.join(
            f"{a.get('family-names', '')}, {a.get('given-names', '')[0]}."
            for a in authors[:5]
        ) + ', et al.'
    else:
        author_str = ', '.join(
            f"{a.get('family-names', '')}, {a.get('given-names', '')}"
            for a in authors
        )

    title = ref.get('title', '')
    journal = ref.get('journal', '')
    year = ref.get('year', '')
    volume = ref.get('volume', '')
    pages = ref.get('pages', '')
    doi = ref.get('doi', '')

    citation_line = f"{author_str} ({year}). _{title}_."
    if journal:
        citation_line += f" **{journal}**"
        if volume:
            citation_line += f", {volume}"
        if pages:
            citation_line += f", {pages}"
        citation_line += '.'
    if doi:
        citation_line += f" [doi: {doi}](https://doi.org/{doi})"

    return f"\n\n## How to cite\n\nIf you use this dataset, please cite:\n\n{citation_line}\n"


def _render_contributors(rc_path):
    with open(rc_path, encoding='utf-8') as f:
        data = json.load(f)
    contributors = data.get('contributors', [])
    if not contributors:
        return ''

    roles_seen = set()
    entries = []
    for c in contributors:
        name = c.get('name', '')
        profile = c.get('profile', '')
        contributions = c.get('contributions', [])
        emojis = ''.join(_CONTRIB_EMOJI.get(r, '') for r in contributions)
        roles_seen.update(contributions)
        if profile:
            entry = f"[{name}]({profile}) {emojis}"
        else:
            entry = f"{name} {emojis}"
        entries.append(entry)

    legend_parts = [
        f"{_CONTRIB_EMOJI[r]} {_CONTRIB_LABEL[r]}"
        for r in _CONTRIB_LABEL
        if r in roles_seen and r in _CONTRIB_EMOJI
    ]
    legend = ' · '.join(legend_parts)

    contributors_str = ' · '.join(entries)
    return f"\n\n## Contributors\n\n{contributors_str}\n\n_{legend}_\n"


def _resolve_stats_key(stats, dotted_key):
    val = stats
    for part in dotted_key.split('.'):
        val = val.get(part, {}) if isinstance(val, dict) else {}
    return val if isinstance(val, dict) else {}


def _render_key_facts(info_path):
    with open(info_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    stats = data.get('stats', {})
    rows = []

    subjects = data.get('subjects', [])
    if subjects:
        cells = ' · '.join(
            f"`{s['id']}` {_STATUS_ICON.get(s.get('status', ''), '')}"
            for s in subjects
        )
        subjects_n = stats.get('subjects_n')
        if subjects_n is not None:
            cells = f"{subjects_n} — {cells}"
        rows.append(('**Subjects**', cells))

    tasks = data.get('tasks', [])
    for i, task in enumerate(tasks):
        emoji = task.get('emoji', '')
        label = task.get('label', '')
        note = task.get('note', '')
        cell = f"{emoji} {label}"
        if note:
            cell += f" — {note}"
        field = '**Tasks**' if i == 0 else ''
        rows.append((field, cell))

    modalities = data.get('modalities', [])
    first_mod = True
    for mod in modalities:
        emoji = mod.get('emoji', '')
        label = mod.get('label', '')
        mod_components = mod.get('components', [])
        stats_key = mod.get('stats_key')

        if stats_key:
            stats_val = _resolve_stats_key(stats, stats_key)
            unit = mod.get('unit', '')
            parts = []
            if 'per_subject_h' in stats_val:
                parts.append(f"{stats_val['per_subject_h']} h/subject")
            elif 'per_subject_unique' in stats_val:
                unit_label = 'h/subject' if unit == 'h' else (unit if unit else 'unique/subject')
                parts.append(f"{stats_val['per_subject_unique']} {unit_label}")
            if parts:
                cell = f"{emoji} {label} — {' · '.join(parts)}"
            else:
                status_icon = _STATUS_ICON.get(mod.get('status', ''), '')
                cell = f"{emoji} {label} {status_icon}"
        elif mod_components:
            comp_str = ', '.join(
                f"{c['label']} {_STATUS_ICON.get(c.get('status', ''), '')}"
                for c in mod_components
            )
            cell = f"{emoji} {label} ({comp_str})"
        else:
            status_icon = _STATUS_ICON.get(mod.get('status', ''), '')
            cell = f"{emoji} {label} {status_icon}"
        field = '**Data**' if first_mod else ''
        first_mod = False
        rows.append((field, cell))

    if not rows:
        return ''

    lines = ['', '', '## Key facts', '', '| | |', '|---|---|']
    for field, cell in rows:
        lines.append(f'| {field} | {cell} |')
    lines.append('')

    return '\n'.join(lines)


def _extract_component_title(content):
    for i, line in enumerate(content.split('\n')):
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', m.group(2).strip())
            rest = '\n'.join(content.split('\n')[i + 1:]).lstrip('\n')
            return level, title, rest
    return None, None, content


def _shift_headings(text, shift):
    if shift <= 0:
        return text
    return re.sub(r'^(#{1,6})(?= )', lambda m: '#' * (len(m.group(1)) + shift), text, flags=re.MULTILINE)


def _render_components_row(components):
    """Single table row listing all components with appropriate links."""
    parts = []
    for stem, path, kind in components:
        content = path.read_text(encoding='utf-8')
        _, title, _ = _extract_component_title(content)
        display = title if title else stem.title()
        if kind == 'page':
            parts.append(f'[{display}](../contents/{stem.lower()})')
        else:
            anchor = re.sub(r'[^a-z0-9]+', '', display.lower())
            parts.append(f'[{display}](#{anchor})')
    return '| **Components** | ' + ' · '.join(parts) + ' |'


def _render_component_sections(components):
    """Embedded ## Components section for local (section-kind) components only."""
    section_comps = [(s, p) for s, p, k in components if k == 'section']
    if not section_comps:
        return ''
    lines = ['\n\n## Components\n']
    for stem, path in section_comps:
        content = path.read_text(encoding='utf-8')
        level, title, rest = _extract_component_title(content)
        display = title if title else stem.title()
        shift = (3 - level) if level else 0
        body = _shift_headings(rest, shift)
        lines.append(f'\n### {display}\n')
        lines.append(body)
    return '\n'.join(lines)
