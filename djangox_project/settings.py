"""
Django settings for djangox_project project.

Generated by 'django-admin startproject' using Django 2.2.0

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
      raise ImproperlyConfigured('Environment variable "%s" not found.' % name)

# required for geodjango to work under windows
""" if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH'] """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '43)%4yx)aa@a=+_c(fn&kf3g29xax+=+a&key9i=!98zyim=8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'social_django',  # social login
    

    # Third-party
    'allauth',
    'allauth.account',
    'crispy_forms',
    'debug_toolbar',

    # Local
    'users',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # for social login
]
 
ROOT_URLCONF = 'djangox_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <-- social login
                'social_django.context_processors.login_redirect', # <-- social login
            ],
        },
    },
]

WSGI_APPLICATION = 'djangox_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'dogooddeed_db',
        'USER': 'dogooddeed_user',
        'PASSWORD': get_env_variable('AZURE_SQL'),
        'HOST': 'dogooddeed.database.windows.net',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'fi'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('hi', 'hindi')
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Enabled for django-debug-toolbar to work
# https://docs.djangoproject.com/en/2.2/ref/settings/#internal-ips
INTERNAL_IPS = ['127.0.0.1']

AUTH_USER_MODEL = 'users.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django-Allauth Config

LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    'social_core.backends.google.GoogleOAuth2',  # social login google
    'social_core.backends.linkedin.LinkedinOAuth2',  # social login linkedin
    'social_core.backends.facebook.FacebookOAuth2',  # social login facebook
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_variable('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_variable('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = get_env_variable('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = get_env_variable('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = get_env_variable('SOCIAL_AUTH_FACEBOOK_KEY')        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = get_env_variable('SOCIAL_AUTH_FACEBOOK_SECRET')  # App Secret
GOOGLE_MAPS_API_KEY = get_env_variable('GOOGLE_MAPS_API_KEY')
DJANGOCMS_GOOGLEMAP_API_KEY = get_env_variable('GOOGLE_MAPS_API_KEY')
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SITE_ID = 1

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Email setup for Password Reset
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gollnick.bert@gmail.com'
EMAIL_HOST_PASSWORD = get_env_variable('GOLLNICK.BERT_GMAIL.COM')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Bert Gollnick <bert.gollnick@posteo.net>'