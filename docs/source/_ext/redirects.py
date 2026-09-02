"""Emit stub pages at the legacy ReadTheDocs URLs.

The docs used to live on ReadTheDocs under versioned prefixes (``/en/latest/``,
``/latest/``, ``/en/2020-alpha/``, ...).  GitHub Pages serves static files only,
so every legacy URL gets a tiny HTML page that forwards to its current home:

* ``<meta http-equiv="refresh">`` handles browsers without JavaScript,
* an inline script handles the fragment, because a meta refresh drops it and
  because anchors such as ``DATASETS.html#anat`` now live on *different* pages.

The map lives in ``docs/redirects.yaml``; anything not listed there falls
through to ``_extra/404.html``, which applies the same rules generically.
"""

import logging
import os
import posixpath
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

_REDIRECTS_YAML = Path(__file__).resolve().parents[2] / 'redirects.yaml'


def _load_redirects(path=_REDIRECTS_YAML):
    """Read redirects.yaml and normalise it to (version_prefixes, pages)."""
    with open(path, encoding='utf-8') as fh:
        data = yaml.safe_load(fh) or {}
    prefixes = [p.strip('/') for p in data.get('version_prefixes', [''])]
    pages = {}
    for name, spec in (data.get('pages') or {}).items():
        pages[name] = {
            'to': spec['to'],
            'anchors': dict(spec.get('anchors') or {}),
        }
    return prefixes, pages


def _built_pages(outdir):
    """Relative posix paths of every HTML page actually produced by the build."""
    outdir = Path(outdir)
    pages = set()
    for path in outdir.rglob('*.html'):
        rel = path.relative_to(outdir).as_posix()
        if rel.split('/')[0].startswith('_') or rel == '404.html':
            continue
        pages.add(rel)
    return pages


def _relative(target, depth):
    """Path from a stub nested `depth` directories deep to a root-relative target."""
    return posixpath.normpath(posixpath.join('../' * depth, target)) if depth else target


def _render_stub(target, anchors, depth):
    """HTML for a single redirect stub."""
    rel_target = _relative(target, depth)
    rel_anchors = {k: _relative(v, depth) for k, v in sorted(anchors.items())}
    anchor_json = '{' + ', '.join(
        f'"{k}": "{v}"' for k, v in rel_anchors.items()
    ) + '}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Page moved</title>
<link rel="canonical" href="{rel_target}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={rel_target}">
<script>
(function () {{
  var anchors = {anchor_json};
  var fallback = "{rel_target}";
  var hash = window.location.hash.replace(/^#/, "");
  var target = anchors[hash] || (hash ? fallback + "#" + hash : fallback);
  window.location.replace(new URL(target, window.location.href).href);
}})();
</script>
</head>
<body>
<p>This page has moved. See <a href="{rel_target}">the current documentation</a>.</p>
</body>
</html>
"""


def _write_stubs(outdir, prefixes, pages, existing=None):
    """Write every (prefix, legacy page) stub under outdir. Returns paths written."""
    outdir = Path(outdir)
    existing = _built_pages(outdir) if existing is None else set(existing)
    written = []

    for prefix in prefixes:
        depth = len(prefix.split('/')) if prefix else 0

        # explicit legacy page names (ACCESS.html, DATASETS.html, ...)
        targets = {name: (spec['to'], spec['anchors']) for name, spec in pages.items()}
        # current page names under a version prefix: /latest/contents/access.html
        for page in existing:
            targets.setdefault(page, (page, {}))

        for name, (target, anchors) in targets.items():
            rel = posixpath.join(prefix, name) if prefix else name
            if rel in existing:
                continue  # never shadow a real page (e.g. bare AUTHORS.html)
            dest = outdir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(_render_stub(target, anchors, depth), encoding='utf-8')
            written.append(rel)

    return written


def _emit_redirects(app, exception):
    """`build-finished` hook: drop the legacy-URL stubs into the HTML output."""
    if exception is not None or app.builder.format != 'html':
        return
    prefixes, pages = _load_redirects()
    # Take the real page list from the build env rather than scanning the output
    # directory: on a rebuild that directory still holds the previous run's stubs, and
    # treating those as real pages nests prefixes inside prefixes without bound
    # (en/latest/en/latest/...), multiplying the output on every build.
    existing = {f'{docname}.html' for docname in app.env.found_docs}
    existing |= {'genindex.html', 'search.html'}  # builder-generated, not docnames
    written = _write_stubs(app.outdir, prefixes, pages, existing=existing)
    logger.info('redirects: wrote %d legacy URL stubs', len(written))


def setup(app):
    app.connect('build-finished', _emit_redirects)
