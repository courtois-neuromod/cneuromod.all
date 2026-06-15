import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.discovery import _discover_dataset_components, _symlink


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
