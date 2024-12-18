# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ngscopeclient'
copyright = '2024, Andrew Zonenberg'
author = 'Andrew Zonenberg and contributors'
release = '0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinx_subfigure',
]
sphinx_tabs_valid_builders = ['linkcheck']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
numfig = True
numfig_format = {
    'code-block': 'Listing %s',
    'figure': 'Fig. %s',
    'section': 'Section %s',
    'table': 'Table %s',
}
numfig_secnum_depth = 1

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_secnumber_suffix = " "

# -- Options for Latex output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = 'xelatex'
latex_theme = 'manual'
latex_elements = {
    'tableofcontents': r'\tableofcontents',
    'preamble': r'''
\usepackage{tocloft}
\setlength{\cftsecindent}{2em}
\setlength{\cftsecnumwidth}{3.75em}
\setlength{\cftsubsecindent}{4em}
\setlength{\cftsubsecnumwidth}{4.5em}
\renewcommand{\sphinxtableofcontentshook}{}
''',
}
