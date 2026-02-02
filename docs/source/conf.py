# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Code import -------------------------------------------------------------
"""
How this works (sorry it's so scuffed at the moment).

1) Clone and install the hohmannpy repository to somewhere on your system.
2) Change the path in sys.path.insert() to be the hohmannpy repository root.
3) Install all the hohmannpy dependencies in this repository.
4) Change your directory to ..\sphinx in the CMD window and then run ".\make html".

NOTE: Generated .html files appear in \build, if you want to clear this folder run ".\make clean".
NOTE 2: Make sure the Sphinx "just-the-docs" theme is installed.
"""
import sys
sys.path.insert(0, "..\\..\\..\\hohmannpy")
import hohmannpy


# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HohmannPy'
copyright = '2026, Nicholas Hirsch'
author = 'Nicholas Hirsch'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "text": "HohmannPy",
        "image_light": "_static\\square_logo.png",
        "image_dark": "_static\\square_logo.png",
    },
}
html_context = {"default_mode": "dark"}
html_favicon = "_static\\square_logo.png"
html_css_files = [
    'css/custom.css',
]

autodoc_default_options = {
    "show-return-type": False,
}
autodoc_typehints = "none"

napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_include_private_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_use_ivar = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
