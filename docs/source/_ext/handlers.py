from . import discovery
from .renderers import (
    _render_citation,
    _render_component_sections,
    _render_components_row,
    _render_contributors,
    _render_key_facts,
)


def _inject_index(app, docname, source):
    if docname != 'index':
        return
    if discovery._discovered_datasets:
        entries = '\n   '.join(f'datasets/{name}' for name in discovery._discovered_datasets)
        source[0] = source[0].replace('   _datasets_placeholder_', f'   {entries}')
    if discovery._global_components:
        entries = '\n   '.join(f'contents/{stem.lower()}' for stem, _ in discovery._global_components)
        source[0] = source[0].replace('   _components_placeholder_', f'   {entries}')
    else:
        source[0] = source[0].replace('\n   _components_placeholder_', '')


def _inject_dataset_metadata(app, docname, source):
    if not docname.startswith('datasets/'):
        return
    name = docname[len('datasets/'):]
    components = discovery._dataset_components.get(name, [])

    key_facts = ''
    if name in discovery._dataset_info:
        key_facts = _render_key_facts(discovery._dataset_info[name])

    comp_row = _render_components_row(components) if components else ''
    if comp_row:
        if key_facts:
            key_facts = key_facts.rstrip('\n') + '\n' + comp_row + '\n'
        else:
            key_facts = f'\n\n| | |\n|---|---|\n{comp_row}\n'

    extra = key_facts
    if name in discovery._dataset_citation:
        extra += _render_citation(discovery._dataset_citation[name])
    if name in discovery._dataset_contributors:
        extra += _render_contributors(discovery._dataset_contributors[name])

    sections = _render_component_sections(components)

    if extra:
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
    force += [f'contents/{stem.lower()}' for stem, _ in discovery._global_components]
    for name in discovery._dataset_citation:
        force.append(f'datasets/{name}')
        seen.add(name)
    for name in discovery._dataset_contributors:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    for name in discovery._dataset_info:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    for name in discovery._dataset_components:
        if name not in seen:
            force.append(f'datasets/{name}')
            seen.add(name)
    return force


def setup(app):
    app.connect('builder-inited', discovery._auto_discover_datasets)
    app.connect('source-read', _inject_index)
    app.connect('source-read', _inject_dataset_metadata)
    app.connect('env-get-outdated', _always_reread_index)
