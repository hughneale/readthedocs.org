import os
import djcelery
djcelery.setup_loader()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Charlie Leifer', 'coleifer@gmail.com'),
    ('Eric Holscher', 'eric@ericholscher.com'),
)

MANAGERS = ADMINS

SITE_ROOT = '/'.join(os.path.dirname(__file__).split('/')[0:-2])
DOCROOT = os.path.join(SITE_ROOT, 'user_builds')
UPLOAD_ROOT = os.path.join(SITE_ROOT, 'user_uploads')

MEDIA_ROOT = '%s/media/' % (SITE_ROOT)
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

CACHE_BACKEND = 'memcached://localhost:11211/'
CACHE_KEY_PREFIX = 'docs'
CACHE_MIDDLEWARE_SECONDS = 60

LOGIN_REDIRECT_URL = '/dashboard/'
FORCE_WWW = False
#APPEND_SLASH = False

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
SITE_ID = 1
SECRET_KEY = 'asciidick'

ACCOUNT_ACTIVATION_DAYS = 7


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'core.middleware.SubdomainMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    '%s/readthedocs/templates/' % (SITE_ROOT),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',

    # third party apps
    'pagination',
    'registration',
    'profiles',
    'taggit',
    'south',
    'basic.flagging',
    'djcelery',
    'celery_haystack',

    #daniellindsleyrocksdahouse
    'haystack',
    'tastypie',

    # our apps
    'projects',
    'builds',
    'core',
    'rtd_tests',
]

if DEBUG:
    INSTALLED_APPS.append('django_extensions')


#CARROT_BACKEND = "ghettoq.taproot.Database"
CELERY_ALWAYS_EAGER = True
CELERYD_TASK_TIME_LIMIT = 60*60 #60 minutes


DEFAULT_FROM_EMAIL = "no-reply@readthedocs.org"
SESSION_COOKIE_DOMAIN = 'readthedocs.org'

HAYSTACK_SITECONF = 'core.search_sites'
HAYSTACK_SEARCH_ENGINE = 'simple'


AUTH_PROFILE_MODULE = "core.UserProfile"
SOUTH_TESTS_MIGRATE = False

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/profiles/%s/" % o.username
}

INTERNAL_IPS = ('127.0.0.1',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT + "/rtd.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'api': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}
