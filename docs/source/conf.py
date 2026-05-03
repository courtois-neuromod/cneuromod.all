project = 'Courtois NeuroMod'
copyright = '2025, Courtois NeuroMod team'
author = 'Courtois NeuroMod team'
release = 'latest'
master_doc = 'index'

extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_short_title = 'CNeuroMod'
html_logo = 'img/logo_neuromod_black.png'
html_favicon = 'img/logo_neuromod_small.png'
html_static_path = ['_static']

myst_enable_extensions = [
    "colon_fence"
]
myst_heading_anchors = 3

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

import json
import os
import re
import yaml
from pathlib import Path

_discovered_datasets = []
_global_components = []   # [(stem, path), ...] — root-level component pages
_dataset_citation = {}
_dataset_contributors = {}
_dataset_info = {}
_dataset_components = {}  # name -> [(stem, path, kind), ...] where kind='page'|'section'

_CONTRIB_EMOJI = {
    'audio':             '🔊',
    'bug':               '🐛',
    'code':              '💻',
    'data':              '🔣',
    'design':            '🎨',
    'doc':               '📖',
    'financial':         '💰',
    'fundingFinding':    '🔍',
    'ideas':             '🤔',
    'infra':             '🚇',
    'maintenance':       '🚧',
    'mentoring':         '🧑‍🏫',
    'projectManagement': '📆',
    'question':          '💬',
    'research':          '🔬',
    'review':            '👀',
    'security':          '🛡️',
    'talk':              '📢',
    'test':              '⚠️',
    'tool':              '🔧',
    'translation':       '🌍',
    'tutorial':          '✅',
    'userTesting':       '📓',
    'video':             '📹',
}

_CONTRIB_LABEL = {
    'audio':             'audio',
    'bug':               'bug reports',
    'code':              'code',
    'data':              'data',
    'design':            'design',
    'doc':               'documentation',
    'financial':         'funding',
    'fundingFinding':    'funding finding',
    'ideas':             'ideas',
    'infra':             'infrastructure',
    'maintenance':       'maintenance',
    'mentoring':         'mentoring',
    'projectManagement': 'project management',
    'question':          'questions',
    'research':          'research',
    'review':            'review',
    'security':          'security',
    'talk':              'talks',
    'test':              'tests',
    'tool':              'tools',
    'translation':       'translation',
    'tutorial':          'tutorials',
    'userTesting':       'user testing',
    'video':             'video',
}

_STATUS_ICON = {
    'available':     '✅',
    'pending':       '⬜',
    'not_collected': '❌',
}

# Uppercase .md files at the repo root excluded from auto-discovery entirely
_ROOT_MD_EXCLUDE = {'README.md', 'CLAUDE.md'}
# Uppercase .md files that are symlinked but hardcoded in index.rst (kept out of the placeholder)
_ROOT_MD_MANUAL = {'DOWNLOADING.md'}


def _symlink(link_path, target_path, base_dir):
    """Create or refresh a symlink at link_path pointing to target_path (relative to base_dir)."""
    rel = os.path.relpath(str(target_path), base_dir)
    link = str(link_path)
    if os.path.islink(link):
        if os.readlink(link) != rel:
            os.remove(link)
            os.symlink(rel, link)
    else:
        os.symlink(rel, link)


def _discover_dataset_components(dataset_path, global_stems):
    """
    Return [(stem, path, kind), ...] for a dataset, sorted by stem.

    kind='page'    — global component; dataset page links to its own standalone page.
    kind='section' — local/override component; content is embedded in the dataset page.
    """
    ds = Path(dataset_path)
    result = {}

    # Global components that apply (dataset has a matching subdirectory)
    for stem, path in global_stems:
        if (ds / stem.lower()).is_dir():
            result[stem] = (path, 'page')

    # Dataset-local components override globals and add new ones
    for f in sorted(ds.glob('*.md')):
        if not f.stem[0].isupper() or f.name == 'README.md':
            continue
        result[f.stem] = (f, 'section')

    return sorted((stem, path, kind) for stem, (path, kind) in result.items())


def _auto_discover_datasets(app):
    global _discovered_datasets, _global_components
    global _dataset_citation, _dataset_contributors, _dataset_info, _dataset_components

    conf_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(conf_dir, '..', '..'))

    # --- global component pages (root-level uppercase .md files) ---
    components_dir = os.path.join(conf_dir, 'contents')
    os.makedirs(components_dir, exist_ok=True)
    global_comps = []
    for f in sorted(Path(repo_root).glob('*.md')):
        if not f.stem[0].isupper() or f.name in _ROOT_MD_EXCLUDE:
            continue
        link_path = Path(components_dir) / (f.stem.lower() + '.md')
        _symlink(link_path, f, components_dir)
        if f.name not in _ROOT_MD_MANUAL:
            global_comps.append((f.stem, f))
    _global_components = global_comps

    # --- dataset pages ---
    datasets_dir = os.path.join(conf_dir, 'datasets')
    os.makedirs(datasets_dir, exist_ok=True)

    skip = {'docs'}
    found = []
    citation = {}
    contributors = {}
    info = {}
    components = {}

    for name in sorted(os.listdir(repo_root)):
        full_path = os.path.join(repo_root, name)
        if not os.path.isdir(full_path):
            continue
        if name.startswith('.') or name in skip:
            continue
        readme = os.path.join(full_path, 'README.md')
        if not os.path.isfile(readme):
            continue

        link_path = Path(datasets_dir) / (name + '.md')
        _symlink(link_path, Path(readme), datasets_dir)
        found.append(name)

        cff_path = os.path.join(full_path, 'CITATION.cff')
        if os.path.isfile(cff_path):
            citation[name] = cff_path

        rc_path = os.path.join(full_path, '.all-contributorsrc')
        if os.path.isfile(rc_path):
            contributors[name] = rc_path

        info_path = os.path.join(full_path, 'dataset_info.yaml')
        if os.path.isfile(info_path):
            info[name] = info_path

        comps = _discover_dataset_components(full_path, global_comps)
        if comps:
            components[name] = comps

    _discovered_datasets = found
    _dataset_citation = citation
    _dataset_contributors = contributors
    _dataset_info = info
    _dataset_components = components


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


def _render_key_facts(info_path):
    with open(info_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    rows = []

    # Subjects row
    subjects = data.get('subjects', [])
    if subjects:
        cells = ' · '.join(
            f"`{s['id']}` {_STATUS_ICON.get(s.get('status', ''), '')}"
            for s in subjects
        )
        rows.append(('**Subjects**', cells))

    # Duration row
    dur = data.get('duration', {})
    if dur:
        n_min = dur.get('n_sessions_min')
        n_max = dur.get('n_sessions_max')
        h_pp = dur.get('hours_per_participant')
        h_tot = dur.get('hours_total')
        parts = []
        if n_min is not None and n_max is not None:
            parts.append(f"{n_min}–{n_max} sessions")
        elif n_min is not None:
            parts.append(f"{n_min}+ sessions")
        if h_pp is not None:
            parts.append(f"~{h_pp} h/participant")
        if h_tot is not None:
            parts.append(f"~{h_tot} h total")
        if parts:
            rows.append(('**Duration**', ' · '.join(parts)))

    # Tasks rows
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

    # Modalities rows
    modalities = data.get('modalities', [])
    first_mod = True
    for mod in modalities:
        emoji = mod.get('emoji', '')
        label = mod.get('label', '')
        mod_components = mod.get('components', [])
        if mod_components:
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
            # Link to standalone component page in contents/
            parts.append(f'[{display}](../contents/{stem.lower()})')
        else:
            # Same-page anchor link to embedded section
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


def _inject_index(app, docname, source):
    if docname != 'index':
        return
    if _discovered_datasets:
        entries = '\n   '.join(f'datasets/{name}' for name in _discovered_datasets)
        source[0] = source[0].replace('   _datasets_placeholder_', f'   {entries}')
    if _global_components:
        entries = '\n   '.join(f'contents/{stem.lower()}' for stem, _ in _global_components)
        source[0] = source[0].replace('   _components_placeholder_', f'   {entries}')
    else:
        source[0] = source[0].replace('\n   _components_placeholder_', '')


def _inject_dataset_metadata(app, docname, source):
    if not docname.startswith('datasets/'):
        return
    name = docname[len('datasets/'):]
    components = _dataset_components.get(name, [])

    key_facts = ''
    if name in _dataset_info:
        key_facts = _render_key_facts(_dataset_info[name])

    comp_row = _render_components_row(components) if components else ''
    if comp_row:
        if key_facts:
            key_facts = key_facts.rstrip('\n') + '\n' + comp_row + '\n'
        else:
            key_facts = f'\n\n| | |\n|---|---|\n{comp_row}\n'

    extra = key_facts
    if name in _dataset_citation:
        extra += _render_citation(_dataset_citation[name])
    if name in _dataset_contributors:
        extra += _render_contributors(_dataset_contributors[name])

    sections = _render_component_sections(components)

    if extra:
        # Insert after the first blank line (end of the title heading block)
        pos = source[0].find('\n\n')
        if pos >= 0:
            source[0] = source[0][:pos + 2] + extra.lstrip('\n') + '\n\n' + source[0][pos + 2:]
        else:
            source[0] = extra.lstrip('\n') + '\n\n' + source[0]

    if sections:
        source[0] = source[0].rstrip('\n') + sections


def _always_reread_index(app, env, added, changed, removed):
    # Force re-read of index, component pages, and dataset pages with metadata,
    # so content stays current on incremental builds.
    seen = set()
    force = ['index']
    force += [f'contents/{stem.lower()}' for stem, _ in _global_components]
    for name in _dataset_citation:
        force.append(f'datasets/{name}')
        seen.add(name)
    for name in _dataset_contributors:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    for name in _dataset_info:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    for name in _dataset_components:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    return force


def setup(app):
    app.connect('builder-inited', _auto_discover_datasets)
    app.connect('source-read', _inject_index)
    app.connect('source-read', _inject_dataset_metadata)
    app.connect('env-get-outdated', _always_reread_index)
