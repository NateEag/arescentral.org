# -*- coding: utf-8 -*-
#
# Ares Central documentation build configuration file, created by
# sphinx-quickstart on Fri May 13 20:47:09 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
sys.path.insert(0, os.path.abspath("."))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = "1.0"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "ext.articlelist",
    "ext.feed",
    "ext.issuetracker",
    "ext.youtube",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
template_bridge = 'ext.template_helpers.TemplateBridge'

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
#source_encoding = "utf-8-sig"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Ares Central"
copyright = u"2011, Ares Central"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1"
# The full version, including alpha/beta/rc tags.
release = "1"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ""
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = "%B %d, %Y"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, "()" will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_epilog = """
..  include:: /epilog.rsti
"""


# -- Options for HTML output ---------------------------------------------------

html_theme_path = ["_themes"]
html_theme = "arescentral"
html_theme_options = {
    "accentcolor": "hsl(0, 66%, 50%)",
    "darkaccentcolor": "hsl(0, 66%, 33%)",
    "nosidebar": True,
}

html_title = "Ares Central"
#html_short_title = None
#html_logo = None
html_favicon = "favicon.ico"

html_static_path = ["_static"]

#html_last_updated_fmt = "%b %d, %Y"
#html_show_sphinx = True
#html_show_copyright = True

#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

#html_additional_pages = {}

html_domain_indices = False
html_use_index = False
#html_split_index = False

html_show_sourcelink = False

html_add_permalinks = False

#html_use_opensearch = ""

html_file_suffix = ".html"

# Output file base name for HTML help builder.
htmlhelp_basename = "AresCentral"

feed_title = u"News — Ares Central"
feed_base_url = "http://arescentral.org"
feed_filename = "news.atom"

issuetracker = "google code"
issuetracker_project = "antares"
issuetracker_issue_pattern = "Issue (\d+)"
