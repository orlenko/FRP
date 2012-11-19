import os, sys
# Django settings for app project.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)



MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(BASE_DIR, "pages", "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '04$8(dg8x$o=7e5!r9q_)pgovm-7g0m0ujg+$qb@sg#lgc)(_t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
    #'fiber.middleware.PageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'fiber.context_processors.page_info',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    # and sitemaps
    'django.contrib.sitemaps',


    # template module
    "pages",

    # dependencies
    "south",
    "pagination",
    'mptt',
    'compressor',
    "haystack",
    'fiber',
    "gunicorn",
    "timezones",

    # site packages
    "memdir", # member directory with import
    "rose", # slideshow
    "news",
    "tinymce", # for the blog
    "ckeditor",
    "photologue",
    #"registration", # for registration and some notifications/verifications
    "uni_form", # for nice forms
    #"notification",
    "whoosh",

    # Mapping
    "easy_maps",

    # databrowse Beta
    #"django.contrib.databrowse",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# FIBER Site settings
FIBER_DEFAULT_TEMPLATE = 'base.html'
FIBER_TEMPLATE_CHOICES = []

FIBER_EXCLUDE_URLS = []

FIBER_IMAGES_DIR = 'uploads/images'
FIBER_FILES_DIR = 'uploads/files'

FIBER_METADATA_PAGE_SCHEMA = {}
FIBER_METADATA_CONTENT_SCHEMA = {}

COMPRESS = not DEBUG

# HAYSTACK
#HAYSTACK_SITECONF = 'memdir'
#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_WHOOSH_PATH = os.path.join(BASE_DIR, 'whoosh_index')
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    }
}


# Django-Registration Settings
ACCOUNT_ACTIVATION_DAYS = 2

# Notification Queue settings
NOTIFICATION_QUEUE_ALL=True

##EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = '/tmp/bcfrpdev/bcfrpmsg'

EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"

# EASY MAPS
##EASY_MAPS_GOOGLE_KEY = "ABQIAAAA_6YxpRQIVJjIx8daYGWgaRTQFubQ9aXSUmGOI1r5AejNfYy9jhT2sT2ikwmkQE3FyRvw08INWDZvZw"
EASY_MAPS_YAHOO_KEY = "WyrmtwLV34E44wp080AXz6hASJoAezCNlm7O3bF3F7nn2eyeO5PWW4SWMZUkUw4fvzcjLPM-"

CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/"
CKEDITOR_UPLOAD_PATH =  os.path.join(MEDIA_ROOT, 'uploads')

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'kama',
        'toolbar': [
            [      'Source', 'Preview',
              '-', 'PasteText', 'PasteFromWord',
              '-', 'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Strike',
              '-', 'RemoveFormat',
            ],
            [      'NumberedList', 'BulletedList',
              '-', 'Outdent', 'Indent',
              '-', 'Blockquote',
              '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                  'JustifyBlock',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Image', 'Table', 'SpecialChar',
              '-', 'Format', 'TextColor',
              '-', 'Maximize', 'ShowBlocks',
            ]
        ]
    },
}

try:
    from local_settings import *
except ImportError:
    pass

if 'test' in sys.argv:
    try:
        from test_settings import *
    except ImportError:
        pass
