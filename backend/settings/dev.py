"""
Development Django settings for backend project.

Inherits from base.py
"""

from .base import * # Import base settings

# SECURITY WARNING: keep the secret key used in production secret!
# It's recommended to load this from an environment variable even in development
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-rsp+035pavtcs)_r^q5b!i!wdq-g=(b%63e31hqfa#7ooyust9') # Use original key as default

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # Allow local access for development


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Uses the default SQLite database defined in base.py for development

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'e-commerce',
        'USER': 'e-commerce',
        'HOST': 'db',
        'PORT':  5432,
        'PASSWORD': 'e-commerce',
    }
}

# Add any other development-specific settings below
# For example, email backend for testing:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

print("DEBUG:", DEBUG)
print("ALLOWED_HOSTS:", ALLOWED_HOSTS)
print("Using Development Settings")
