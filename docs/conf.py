#!python3

"""
    Configuration for project documentation using Sphinx.
"""

# standard
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(r".."))

# project
from qgis_deployment_toolbelt import __about__

# -- Build environment -----------------------------------------------------
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# -- Project information -----------------------------------------------------
author = __about__.__author__
copyright = __about__.__copyright__
description = __about__.__summary__
project = __about__.__title__
version = release = __about__.__version__

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Sphinx included
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    # 3rd party
    "myst_parser",
    # "sphinx_autodoc_typehints",  # disable because of issue with theme
    "sphinx_click",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = "fr"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "*.csv",
    "samples/*",
    "Thumbs.db",
    ".DS_Store",
    "*env*",
    "libs/*",
    "*.xml",
    "input/*",
    "output/*",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# Theme
# html_favicon = "static/img/qgis_deployment_toolbelt_logo_200px.png"
# html_logo = "static/img/qgis_deployment_toolbelt_logo_200px.png"
html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": __about__.__uri_repository__,
    "show_toc_level": 3,
    "use_edit_page_button": True,
    "use_fullscreen_button": False,
    "use_issues_button": True,
    "use_repository_button": True,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]
}

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = "en"


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}


# -- Extension configuration -------------------------------------------------


# MyST Parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]
# replacement variables
myst_substitutions = {
    "author": author,
    "date_update": datetime.now().strftime("%d %B %Y"),
    "description": description,
    "repo_url": __about__.__uri__,
    "title": project,
    "version": version,
}


myst_heading_anchors = 3

# OpenGraph
ogp_image = (
    f"{__about__.__uri_homepage__}/_images/qgis-deployment-toolbelt_cli_help.png"
)
ogp_site_name = f"{project} - Documentation"
ogp_site_url = __about__.__uri_homepage__
ogp_custom_meta_tags = [
    "<meta name='twitter:card' content='summary_large_image'>",
    f'<meta property="twitter:description" content="{description}" />',
    f'<meta property="twitter:image" content="{ogp_image}" />',
    '<meta property="twitter:site" content="@geojulien" />',
    f'<meta property="twitter:title" content="{project}" />',
]

# -- Options for Sphinx API doc ----------------------------------------------
# run api doc
def run_apidoc(_):
    from sphinx.ext.apidoc import main

    cur_dir = os.path.normpath(os.path.dirname(__file__))
    output_path = os.path.join(cur_dir, "_apidoc")
    modules = os.path.normpath(os.path.join(cur_dir, "../qgis_deployment_toolbelt/"))
    exclusions = ["../input", "../output", "/tests"]
    main(["-e", "-f", "-M", "-o", output_path, modules] + exclusions)


# launch setup
def setup(app):
    app.connect("builder-inited", run_apidoc)
