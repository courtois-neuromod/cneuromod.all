import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.discovery import _auto_discover_datasets, _discover_dataset_components, _symlink
import _ext.discovery as discovery


class TestSymlink:
    def test_creates_symlink(self, tmp_path):
        target = tmp_path / 'target.md'
        target.write_text('hello')
        link = tmp_path / 'subdir' / 'link.md'
        link.parent.mkdir()
        _symlink(link, target, str(link.parent))
        assert os.path.islink(str(link))
        assert os.path.realpath(str(link)) == str(target)

    def test_refreshes_stale_symlink(self, tmp_path):
        old_target = tmp_path / 'old.md'
        old_target.write_text('old')
        new_target = tmp_path / 'new.md'
        new_target.write_text('new')
        link = tmp_path / 'link.md'
        # Create a stale symlink pointing to old_target
        os.symlink(os.path.relpath(str(old_target), str(tmp_path)), str(link))
        # Now refresh to point to new_target
        _symlink(link, new_target, str(tmp_path))
        assert os.readlink(str(link)) == os.path.relpath(str(new_target), str(tmp_path))


class TestDiscoverDatasetComponents:
    def test_page_kind_for_global_stem_with_matching_dir(self, tmp_path):
        # Dataset has a 'fmriprep' subdirectory matching a global component stem
        dataset = tmp_path / 'mydataset'
        dataset.mkdir()
        (dataset / 'fmriprep').mkdir()

        global_page = tmp_path / 'Fmriprep.md'
        global_page.write_text('# fMRIPrep')
        global_stems = [('Fmriprep', global_page)]

        result = _discover_dataset_components(dataset, global_stems)
        assert len(result) == 1
        stem, path, kind = result[0]
        assert stem == 'Fmriprep'
        assert kind == 'page'

    def test_section_kind_for_local_uppercase_md(self, tmp_path):
        dataset = tmp_path / 'mydataset'
        dataset.mkdir()
        local_md = dataset / 'Methods.md'
        local_md.write_text('## Methods\n\nDetails.')

        result = _discover_dataset_components(dataset, [])
        assert len(result) == 1
        stem, path, kind = result[0]
        assert stem == 'Methods'
        assert kind == 'section'

    def test_readme_excluded_from_components(self, tmp_path):
        dataset = tmp_path / 'mydataset'
        dataset.mkdir()
        (dataset / 'README.md').write_text('# README')
        result = _discover_dataset_components(dataset, [])
        assert result == []

    def test_lowercase_md_excluded(self, tmp_path):
        dataset = tmp_path / 'mydataset'
        dataset.mkdir()
        (dataset / 'notes.md').write_text('# notes')
        result = _discover_dataset_components(dataset, [])
        assert result == []

    def test_local_overrides_global(self, tmp_path):
        # A local Methods.md overrides a hypothetical global Methods stem
        dataset = tmp_path / 'mydataset'
        dataset.mkdir()
        (dataset / 'methods').mkdir()  # matches global stem 'Methods'
        local_md = dataset / 'Methods.md'
        local_md.write_text('## Methods local')

        global_page = tmp_path / 'Methods.md'
        global_page.write_text('# Methods global')
        global_stems = [('Methods', global_page)]

        result = _discover_dataset_components(dataset, global_stems)
        assert len(result) == 1
        stem, path, kind = result[0]
        assert kind == 'section'  # local overrides global
        assert path == local_md


class TestAutoDiscoverDatasets:
    def _run_discovery(self, repo_root, monkeypatch):
        """Run _auto_discover_datasets with a patched conf dir pointing at repo_root.

        Mirror the real layout: repo_root/docs/source/_ext/discovery.py
        so that conf_dir/../../.. resolves back to repo_root.
        """
        fake_ext_dir = repo_root / 'docs' / 'source' / '_ext'
        fake_ext_dir.mkdir(parents=True, exist_ok=True)
        monkeypatch.setattr(discovery, '__file__', str(fake_ext_dir / 'discovery.py'))
        discovery._auto_discover_datasets(None)

    def test_readme_dataset_uses_symlink(self, tmp_path, monkeypatch):
        ds = tmp_path / 'myds'
        ds.mkdir()
        (ds / 'README.md').write_text('# My Dataset\n\nContent.')
        (ds / 'dataset_info.yaml').write_text('{}')

        self._run_discovery(tmp_path, monkeypatch)

        page = tmp_path / 'docs' / 'source' / 'datasets' / 'myds.md'
        assert page.is_symlink()
        assert 'myds' in discovery._discovered_datasets
        assert 'myds' in discovery._dataset_readme

    def test_info_only_dataset_writes_stub(self, tmp_path, monkeypatch):
        ds = tmp_path / 'myds'
        ds.mkdir()
        (ds / 'dataset_info.yaml').write_text('{}')

        self._run_discovery(tmp_path, monkeypatch)

        page = tmp_path / 'docs' / 'source' / 'datasets' / 'myds.md'
        assert page.exists() and not page.is_symlink()
        assert page.read_text(encoding='utf-8') == '# myds\n'
        assert 'myds' in discovery._discovered_datasets
        assert 'myds' not in discovery._dataset_readme

    def test_no_info_no_readme_skipped(self, tmp_path, monkeypatch):
        ds = tmp_path / 'myds'
        ds.mkdir()

        self._run_discovery(tmp_path, monkeypatch)

        assert 'myds' not in discovery._discovered_datasets

    def test_readme_only_still_discovered(self, tmp_path, monkeypatch):
        ds = tmp_path / 'myds'
        ds.mkdir()
        (ds / 'README.md').write_text('# My Dataset\n')

        self._run_discovery(tmp_path, monkeypatch)

        assert 'myds' in discovery._discovered_datasets
        assert 'myds' in discovery._dataset_readme
