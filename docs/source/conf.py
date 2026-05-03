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

autosectionlabel_prefix_document = True

import json
import os
import yaml

_discovered_datasets = []
_dataset_citation = {}
_dataset_contributors = {}
_dataset_info = {}

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


def _auto_discover_datasets(app):
    global _discovered_datasets, _dataset_citation, _dataset_contributors, _dataset_info
    conf_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(conf_dir, '..', '..'))
    datasets_dir = os.path.join(conf_dir, 'datasets')
    os.makedirs(datasets_dir, exist_ok=True)

    skip = {'docs'}
    found = []
    citation = {}
    contributors = {}
    info = {}

    for name in sorted(os.listdir(repo_root)):
        full_path = os.path.join(repo_root, name)
        if not os.path.isdir(full_path):
            continue
        if name.startswith('.') or name in skip:
            continue
        readme = os.path.join(full_path, 'README.md')
        if not os.path.isfile(readme):
            continue

        link_path = os.path.join(datasets_dir, name + '.md')
        link_target = os.path.relpath(readme, datasets_dir)
        if os.path.islink(link_path):
            if os.readlink(link_path) == link_target:
                found.append(name)
            else:
                os.remove(link_path)
                os.symlink(link_target, link_path)
                found.append(name)
        else:
            os.symlink(link_target, link_path)
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

    _discovered_datasets = found
    _dataset_citation = citation
    _dataset_contributors = contributors
    _dataset_info = info


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
        components = mod.get('components', [])
        if components:
            comp_str = ', '.join(
                f"{c['label']} {_STATUS_ICON.get(c.get('status', ''), '')}"
                for c in components
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


def _inject_datasets(app, docname, source):
    if docname != 'index' or not _discovered_datasets:
        return
    entries = '\n   '.join(f'datasets/{name}' for name in _discovered_datasets)
    source[0] = source[0].replace('   _datasets_placeholder_', f'   {entries}')


def _inject_dataset_metadata(app, docname, source):
    if not docname.startswith('datasets/'):
        return
    name = docname[len('datasets/'):]
    extra = ''
    if name in _dataset_info:
        extra += _render_key_facts(_dataset_info[name])
    if name in _dataset_citation:
        extra += _render_citation(_dataset_citation[name])
    if name in _dataset_contributors:
        extra += _render_contributors(_dataset_contributors[name])
    if extra:
        # Insert after the first blank line (end of the title heading block)
        pos = source[0].find('\n\n')
        if pos >= 0:
            source[0] = source[0][:pos + 2] + extra.lstrip('\n') + '\n\n' + source[0][pos + 2:]
        else:
            source[0] = extra.lstrip('\n') + '\n\n' + source[0]


def _always_reread_index(app, env, added, changed, removed):
    # Force re-read of index and any dataset page that has metadata files,
    # so citation/contributor content stays current on incremental builds.
    force = ['index']
    force += [f'datasets/{name}' for name in _dataset_citation]
    force += [f'datasets/{name}' for name in _dataset_contributors if name not in _dataset_citation]
    force += [f'datasets/{name}' for name in _dataset_info if name not in _dataset_citation and name not in _dataset_contributors]
    return force


def setup(app):
    app.connect('builder-inited', _auto_discover_datasets)
    app.connect('source-read', _inject_datasets)
    app.connect('source-read', _inject_dataset_metadata)
    app.connect('env-get-outdated', _always_reread_index)
