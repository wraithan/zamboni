import sys
import os
sys.path.append(os.path.abspath('../..'))
from docs.conf import *  # noqa


master_doc = 'index'

project = u'marketplace-api'
version = release = '1.0'  # Should correspond to the API version number

html_theme_path = ['../_themes']
html_static_path = ['../_static']
