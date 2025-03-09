from .settings_default import *

CACHEOPS = {
    '*.*': {'ops': ()},
}
CACHEOPS_ENABLED = False
STORAGES = {
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'
        },
}
