# -*- coding: utf-8 -*-
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Ansible RayCrafter'
copyright = u'2015, David Zuber'
author = u'David Zuber'

version = '2.3.0'
release = '2.3.0'

language = None

exclude_patterns = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'AnsibleRayCrafterdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
  (master_doc, 'AnsibleRayCrafter.tex', u'Ansible RayCrafter Documentation',
   u'David Zuber', 'manual'),
]

# -- Intersphinx Config ---------------------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/', None),
                       'raycrafterdoc': ('http://raycrafter.readthedocs.org/en/master/', None),
}
