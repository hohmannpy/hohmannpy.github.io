# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Code import -------------------------------------------------------------
import hohmannpy

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HohmannPy'
copyright = '2026, Nicholas Hirsch'
author = 'Nicholas Hirsch'
release = 'v0.0.7'

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
autodoc_mock_imports = ['numpy', 'scipy', 'pygfx', 'pandas', 'imageio', 'pylinalg', 'rendercanvas']

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
