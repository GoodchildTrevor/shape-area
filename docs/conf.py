import os
import sys

# -- Path setup ------------------------------------------------------

# Добавляем src/ в путь
sys.path.insert(0, os.path.abspath('../../src'))

import shape_area

# -- Project information ---------------------------------------------

project = 'Shape Area'
copyright = '2025, Ruslan Kondrashuk'
author = 'Ruslan Kondrashuk'
version = shape_area.__version__
release = shape_area.__version__

# -- General configuration -------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'
source_encoding = 'utf-8'

# -- Options for HTML output -----------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc settings ------------------------------------------------

autodoc_member_order = 'bysource'
