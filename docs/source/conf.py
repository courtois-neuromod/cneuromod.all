project = 'Courtois NeuroMod'
copyright = '2025, Courtois NeuroMod team'
author = 'Courtois NeuroMod team'
release = 'latest'
master_doc = 'index'

extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['cneuromod_references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'label'

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 2,
}
html_short_title = 'CNeuroMod'
html_logo = 'img/logo_neuromod_black.png'
html_favicon = 'img/logo_neuromod_small.png'
html_static_path = ['_static']
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
