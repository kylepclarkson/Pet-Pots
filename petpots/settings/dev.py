# Extends base settings
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_dev')
MEDIA_URL = '/media_dev/'