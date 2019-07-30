from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g&@3m=9r&c0neas)6t#63wml)!y-u@pu72xnze726o5m3=80(*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
