# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'misc'
copyright = '2025, sspuiip'
author = 'sspuiip'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx',
              'sphinxcontrib.mermaid',     
              'sphinx_copybutton',    
              'sphinx_design',    
              'sphinx_togglebutton',
              'sphinx.ext.mathjax',
              'sphinx-mathjax-offline',
              'myst_nb'] #,'rst2pdf.pdfbuilder']


templates_path = ['_templates']
exclude_patterns = ['_build']

language = 'zh_CN'

source_suffix = {
    '.rst': 'restructuredtext',
    #'.txt': 'markdown',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb'
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature' # furo sphinx_book_theme pydata_sphinx_theme nature sphinx_rtd_theme
html_static_path = ['_static']




# -- Extension configuration -------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- mermaid
mermaid_version = '10.8.0'


numfig = True
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s',
    'equation': '式 %s'  # 自定义公式编号前缀:ml-citation{ref="5" data="citationList"}
}
