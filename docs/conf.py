import sprockets_influxdb

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]

master_doc = 'index'

project = 'sprockets-influxdb'
copyright = '2016-2019, AWeber Communications'
author = 'AWeber Communications'

release = sprockets_influxdb.__version__
version = '.'.join(release.split('.')[0:1])

pygments_style = 'sphinx'
htmlhelp_basename = 'sprockets-influxdbdoc'
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'tornado': ('https://www.tornadoweb.org/en/stable/', None)
}
