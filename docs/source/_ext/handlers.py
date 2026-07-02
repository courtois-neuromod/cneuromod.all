from tabulate import tabulate
import yaml

from . import discovery
from .renderers import (
    _render_citation,
    _render_component_sections,
    _render_components_row,
    _render_contributors,
    _render_key_facts,
    _render_dataset_table,
    _render_dataset_stats_table,
    _render_unreleased_warning,
)


def _inject_index(app, docname, source):
    pass


def _inject_datasets_index(app, docname, source):
    if docname != 'contents/datasets':
        return
    if discovery._discovered_datasets:
        entries = '\n   '.join(f'../datasets/{name}' for name in discovery._discovered_datasets)
        source[0] = source[0].replace('   _datasets_toc_placeholder_', f'   {entries}')
    else:
        source[0] = source[0].replace('\n   _datasets_toc_placeholder_', '')


def _inject_datasets_tables(app, docname, source):
    if docname != 'contents/components':
        return
    if discovery._discovered_datasets:
        df = _render_dataset_table(discovery)
        rst_table = tabulate(df, headers='keys', tablefmt='rst')
        source[0] = source[0].replace('_components_table_placeholder_', f'{rst_table}')
    else:
        source[0] = source[0].replace('\n_components_table_placeholder_', '')

def _inject_components_index(app, docname, source):
    if docname != 'contents/components':
        return
    all_stems = sorted(
        {stem.lower() for stem, _ in discovery._global_components}
        | {stem.lower() for stem, _, _ in discovery._local_components}
    )
    if all_stems:
        entries = '\n   '.join(all_stems)
        source[0] = source[0].replace('   _components_toc_placeholder_', f'   {entries}')
    else:
        source[0] = source[0].replace('\n   _components_toc_placeholder_', '')


def _inject_dataset_stats_table(app, docname, source):
    if docname != 'contents/datasets':
        return
    if discovery._discovered_datasets:
        df = _render_dataset_stats_table(discovery)
        rst_table = tabulate(df, headers='keys', tablefmt='rst')
        source[0] = source[0].replace('_datasets_table_placeholder_', rst_table)
    else:
        source[0] = source[0].replace('\n_datasets_table_placeholder_', '')


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

    if name not in discovery._dataset_readme:
        source[0] = source[0].rstrip('\n') + _render_unreleased_warning()



def _always_reread_index(app, env, added, changed, removed):
    # Force re-read of index, component pages, and dataset pages with metadata,
    # so content stays current on incremental builds.
    seen = set()
    force = ['index', 'contents/components', 'contents/datasets']
    force += [f'contents/{stem.lower()}' for stem, _ in discovery._global_components]
    force += [f'contents/{stem.lower()}' for stem, _, _ in discovery._local_components]
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
    app.connect('source-read', _inject_components_index)
    app.connect('source-read', _inject_datasets_index)
    app.connect('source-read', _inject_datasets_tables)
    app.connect('source-read', _inject_dataset_stats_table)
    app.connect('source-read', _inject_dataset_metadata)
    app.connect('env-get-outdated', _always_reread_index)
