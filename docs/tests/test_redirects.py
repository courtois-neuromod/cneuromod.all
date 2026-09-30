import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.redirects import (
    _built_pages,
    _load_redirects,
    _relative,
    _render_stub,
    _write_stubs,
)

DOCS = Path(__file__).parent.parent
SOURCE = DOCS / 'source'

# URLs listed in issue #21, with the host and version prefix kept as published.
ISSUE_21_URLS = [
    '/',
    '/en/2020-alpha/MEG.html',
    '/en/2020-alpha/MRI.html',
    '/en/2020-alpha/DATASETS.html#datasets',
    '/en/2020-alpha/MRI.html#mri',
    '/en/2020-alpha/MRI.html#physiological-measures',
    '/en/latest/ACCESS.html',
    '/en/latest/AUTHORS.html',
    '/en/latest/DATASETS.html#anat',
    '/en/latest/DATASETS.html#floc',
    '/en/latest/DATASETS.html#friends',
    '/en/latest/DATASETS.html#harrypotter',
    '/en/latest/DATASETS.html#hcptrt',
    '/en/latest/DATASETS.html#movie10',
    '/en/latest/DATASETS.html#retinotopy',
    '/en/latest/DATASETS.html#shinobi',
    '/en/latest/DATASETS.html#shinobi-training',
    '/en/latest/DATASETS.html#things',
]


@pytest.fixture(scope='module')
def redirects():
    return _load_redirects()


class TestConfig:
    def test_parses(self, redirects):
        prefixes, pages = redirects
        assert '' in prefixes
        assert 'en/latest' in prefixes
        assert 'DATASETS.html' in pages

    def test_targets_resolve_to_real_documents(self, redirects):
        """Every target names a document that Sphinx will build."""
        _, pages = redirects
        targets = []
        for spec in pages.values():
            targets.append(spec['to'])
            targets.extend(spec['anchors'].values())

        for target in targets:
            doc = target.split('#')[0][: -len('.html')]
            candidates = [
                SOURCE / f'{doc}.rst',
                SOURCE / f'{doc}.md',
                # datasets/*.md are symlinked in at build time by discovery
                DOCS.parent / doc.replace('datasets/', '', 1) / 'README.md',
            ]
            assert any(c.exists() for c in candidates), f'{target} has no source document'


class TestRelative:
    def test_root_level_target_is_unchanged(self):
        assert _relative('contents/access.html', 0) == 'contents/access.html'

    def test_nested_stub_climbs_back_to_the_root(self):
        assert _relative('contents/access.html', 2) == '../../contents/access.html'


class TestRenderStub:
    def test_meta_refresh_and_canonical_point_at_the_target(self):
        html = _render_stub('contents/mri.html', {}, 2)
        assert 'url=../../contents/mri.html' in html
        assert '<link rel="canonical" href="../../contents/mri.html">' in html

    def test_anchor_map_is_embedded_and_relative(self):
        html = _render_stub('contents/datasets.html', {'anat': 'datasets/anat.html'}, 2)
        assert '"anat": "../../datasets/anat.html"' in html


class TestWriteStubs:
    def test_writes_prefixed_stubs(self, tmp_path):
        (tmp_path / 'contents').mkdir()
        (tmp_path / 'contents' / 'access.html').write_text('real page')

        written = _write_stubs(
            tmp_path,
            ['', 'en/latest'],
            {'ACCESS.html': {'to': 'contents/access.html', 'anchors': {}}},
        )

        assert 'ACCESS.html' in written
        assert 'en/latest/ACCESS.html' in written
        # current page names are mirrored under the version prefix too
        assert 'en/latest/contents/access.html' in written
        assert 'url=../../contents/access.html' in (
            tmp_path / 'en/latest/ACCESS.html'
        ).read_text()

    def test_never_overwrites_a_real_page(self, tmp_path):
        (tmp_path / 'AUTHORS.html').write_text('real page')

        _write_stubs(tmp_path, [''], {'AUTHORS.html': {'to': 'AUTHORS.html', 'anchors': {}}})

        assert (tmp_path / 'AUTHORS.html').read_text() == 'real page'

    def test_ignores_underscore_directories(self, tmp_path):
        (tmp_path / '_static').mkdir()
        (tmp_path / '_static' / 'thing.html').write_text('asset')
        assert _built_pages(tmp_path) == set()


class TestIssue21:
    def test_every_published_url_is_covered(self, tmp_path, redirects):
        prefixes, pages = redirects
        for page in ['index.html', 'contents/access.html', 'AUTHORS.html',
                     'contents/datasets.html', 'contents/mri.html',
                     'contents/training.html'] + [
                         f'datasets/{d}.html' for d in
                         ('anat floc friends harrypotter hcptrt movie10 '
                          'retinotopy shinobi things').split()]:
            dest = tmp_path / page
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text('real page')

        _write_stubs(tmp_path, prefixes, pages)

        for url in ISSUE_21_URLS:
            path, _, anchor = url.lstrip('/').partition('#')
            path = path or 'index.html'
            stub = tmp_path / path
            assert stub.exists(), f'{url}: no page served at {path}'
            if anchor:
                html = stub.read_text()
                spec = pages.get(Path(path).name, {})
                if anchor in spec.get('anchors', {}):
                    assert f'"{anchor}"' in html, f'{url}: anchor not mapped'
