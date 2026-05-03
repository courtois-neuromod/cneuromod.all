# CNeuroMod documentation

Built with [Sphinx](https://www.sphinx-doc.org/) + [MyST Parser](https://myst-parser.readthedocs.io/) and hosted on [ReadTheDocs](https://docs.cneuromod.ca).

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
├── requirements.txt      # RTD-compatible deps (mirrors pyproject.toml)
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
