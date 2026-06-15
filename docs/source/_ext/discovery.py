import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

from .constants import _ROOT_MD_EXCLUDE, _ROOT_MD_MANUAL
from . import validator as _validator

_discovered_datasets = []
_global_components = []   # [(stem, path), ...] — root-level component pages
_local_components = []    # [(stem, path, dataset_name), ...] — dataset-specific component pages
_dataset_citation = {}
_dataset_contributors = {}
_dataset_info = {}
_dataset_components = {}  # name -> [(stem, path, kind), ...] where kind='page'|'section'


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

    for stem, path in global_stems:
        if (ds / stem.lower()).is_dir():
            result[stem] = (path, 'page')

    for f in sorted(ds.glob('*.md')):
        if not f.stem[0].isupper() or f.name == 'README.md':
            continue
        result[f.stem] = (f, 'section')

    return sorted((stem, path, kind) for stem, (path, kind) in result.items())


def _auto_discover_datasets(app):
    global _discovered_datasets, _global_components, _local_components
    global _dataset_citation, _dataset_contributors, _dataset_info, _dataset_components

    conf_dir = os.path.dirname(os.path.abspath(__file__))
    # _ext/ is one level below source/, which is two levels below the repo root
    repo_root = os.path.abspath(os.path.join(conf_dir, '..', '..', '..'))
    source_dir = os.path.abspath(os.path.join(conf_dir, '..'))

    # --- global component pages (root-level uppercase .md files) ---
    components_dir = os.path.join(source_dir, 'contents')
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
    datasets_dir = os.path.join(source_dir, 'datasets')
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

        rc_path = os.path.join(full_path, 'contributors.json')
        if os.path.isfile(rc_path):
            contributors[name] = rc_path

        info_path = os.path.join(full_path, 'dataset_info.yaml')
        if os.path.isfile(info_path):
            info[name] = info_path

        comps = _discover_dataset_components(full_path, global_comps)
        if comps:
            components[name] = comps

    # Promote section-kind components to standalone pages in contents/
    local_comps = []
    global_stems_set = {stem.lower() for stem, _ in global_comps}
    for name, comps in list(components.items()):
        updated = []
        for stem, path, kind in comps:
            if kind == 'section' and stem.lower() not in global_stems_set:
                link_path = Path(components_dir) / (stem.lower() + '.md')
                _symlink(link_path, path, components_dir)
                local_comps.append((stem, path, name))
                updated.append((stem, path, 'page'))
            else:
                updated.append((stem, path, kind))
        components[name] = updated

    _discovered_datasets = found
    _dataset_citation = citation
    _dataset_contributors = contributors
    _dataset_info = info
    _dataset_components = components
    _local_components = local_comps

    schema = _validator._load_schema()
    for name, info_path in info.items():
        for err in _validator.validate_dataset_info(info_path, schema):
            logger.warning(f"[{name}] dataset_info.yaml stats: {err}")
