project = 'Courtois NeuroMod'
copyright = '2025, Courtois NeuroMod team'
author = 'Courtois NeuroMod team'
release = 'latest'
master_doc = 'index'

extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'sphinxcontrib.bibtex',
    'sphinx_design',
]

bibtex_bibfiles = ['cneuromod_references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'label'

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_theme_options = {
    'navigation_with_keys': True,
    # furo resolves these against html_static_path; img/ is copied to _static/ below
    'light_logo': 'logo_neuromod_black.png',
    'dark_logo': 'logo_neuromod_white.png',
}
html_title = 'docs @latest'
html_short_title = 'CNeuroMod'
html_favicon = 'img/logo_neuromod_small.png'
# img/ is listed so furo can reach the light/dark logo pair from _static/
html_static_path = ['_static', 'img']
# CNAME, .nojekyll and the 404 catch-all, copied verbatim to the site root
html_extra_path = ['_extra']
html_css_files = ['custom.css']

myst_enable_extensions = [
    "colon_fence"
]
myst_heading_anchors = 3

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _ext.handlers import setup  # noqa: F401
