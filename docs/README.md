# CNeuroMod documentation

Built with [Sphinx](https://www.sphinx-doc.org/) + [MyST Parser](https://myst-parser.readthedocs.io/) and
deployed to GitHub Pages at [docs.cneuromod.ca](https://docs.cneuromod.ca) by
`.github/workflows/docs.yml` on every push to `main`.

## Local development

Requires [uv](https://docs.astral.sh/uv/).

```bash
# Install dependencies (one-time)
uv sync

# Build HTML
uv run make html

# View result
xdg-open build/html/index.html   # Linux
open build/html/index.html        # macOS
```

Clean build (required when changing the TOC):

```bash
rm -rf build/ && uv run make html
```

## Adding pybids optional dependencies

```bash
uv sync --extra pybids
```

## File structure

```
docs/
├── source/
│   ├── conf.py           # Sphinx config
│   ├── index.rst         # Main table of contents
│   ├── OVERVIEW.rst      # Landing page
│   ├── AUTHORS.md        # Team
│   ├── ACKNOWLEDGMENT.md # Citation & license
│   ├── img/              # Logos
│   └── _static/          # Ethics docs, MRI protocols, posters
├── pyproject.toml        # Dependencies (managed by uv)
└── Makefile
```

## Adding dataset-specific docs

Dataset docs live next to the data they describe (e.g., `friends/docs/index.md`).
To include them in the central build, create a relative symlink inside `docs/source/`:

```bash
mkdir -p docs/source/datasets
ln -s ../../../../friends/docs/index.md docs/source/datasets/friends.md
```

Then add the entry to `docs/source/index.rst`:

```rst
.. toctree::

   datasets/friends
```

## Adding generated content (pybids)

Scripts that auto-generate documentation (e.g., participant tables) live in `docs/scripts/`.
Run them before building:

```bash
python docs/scripts/generate_participants.py
uv run make html
```

On ReadTheDocs, add a pre-build step in `.readthedocs.yaml`:

```yaml
build:
  jobs:
    pre_build:
      - python docs/scripts/generate_participants.py
```

## Hosting and legacy URLs

The site used to be built by ReadTheDocs under versioned prefixes
(`/en/latest/`, `/latest/`, `/en/2020-alpha/`, ...). GitHub Pages serves static files
only — there are no server-side redirects — so the build emits a small forwarding page
at every legacy URL:

- `redirects.yaml` maps old page names (`ACCESS.html`, `DATASETS.html`, ...) to their
  current home, with per-anchor overrides where a section became its own page
  (`DATASETS.html#things` → `datasets/things.html`).
- `source/_ext/redirects.py` writes those stubs into the build on `build-finished`,
  once per version prefix, and also mirrors every current page under each prefix so
  `/latest/contents/access.html` keeps working. A stub never overwrites a real page.
- `source/_extra/` is copied verbatim to the site root: `CNAME` (required — with a
  workflow-based Pages build the custom domain must ship inside the artifact),
  `.nojekyll`, and `404.html`, a catch-all applying the same rules to anything the
  stubs miss.

Add an entry to `redirects.yaml` whenever a page is renamed or moved.

### DNS / Netlify (one-time cutover, done outside this repo)

1. Repoint the `docs.cneuromod.ca` CNAME from `readthedocs.io` to
   `courtois-neuromod.github.io`, then set the custom domain under
   Settings → Pages and wait for "Enforce HTTPS".
2. Retire the ReadTheDocs project `courtois-neuromod-docs`.
3. Keep the Netlify site in `courtois-neuromod/cneuromod.ca` deployed as a pure
   redirector, with `static/_redirects`:

   ```
   /access/access/*         https://docs.cneuromod.ca/contents/access.html      301!
   /gallery/datasets/*      https://docs.cneuromod.ca/contents/datasets.html    301!
   /carousel/acquisitions/* https://docs.cneuromod.ca/contents/mri.html         301!
   /collaborators/*         https://docs.cneuromod.ca/AUTHORS.html              301!
   /about/*                 https://docs.cneuromod.ca/                          301!
   /sections/*              https://docs.cneuromod.ca/                          301!
   /posts/*                 https://docs.cneuromod.ca/                          301!
   /*                       https://docs.cneuromod.ca/:splat                    301!
   ```
