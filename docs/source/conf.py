project = 'Courtois NeuroMod'
copyright = '2025, Courtois NeuroMod team'
author = 'Courtois NeuroMod team'
release = 'latest'
master_doc = 'index'

extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_short_title = 'CNeuroMod'
html_logo = 'img/logo_neuromod_black.png'
html_favicon = 'img/logo_neuromod_small.png'
html_static_path = ['_static']

myst_enable_extensions = [
    "colon_fence"
]

autosectionlabel_prefix_document = True
