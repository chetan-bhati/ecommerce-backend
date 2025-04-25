"""
Production Django settings for backend project.

Inherits from base.py
"""

from .base import * # Import base settings
import os

# SECURITY WARNING: keep the secret key used in production secret!
# Load from environment variable; raise error if not set in production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("No DJANGO_SECRET_KEY set for production environment")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Configure allowed hosts for production (replace with your actual domain(s))
# Example: ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']:
     print("Warning: DJANGO_ALLOWED_HOSTS environment variable not set or empty.")
     # Provide a default or raise an error depending on policy
     # ALLOWED_HOSTS = ['example.com'] # Example default
     # raise ValueError("DJANGO_ALLOWED_HOSTS must be set in production")


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Configure your production database here (e.g., PostgreSQL, MySQL)
# Example for PostgreSQL using environment variables:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT', 5432),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#     }
# }

# Using SQLite for now, but strongly recommend a robust DB for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod.db.sqlite3', # Use a separate DB file for prod
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# Define STATIC_ROOT for collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/' # Ensure STATIC_URL is defined (usually in base.py)

# Add other production-specific settings below
# For example, security settings:
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

print("DEBUG:", DEBUG)
print("ALLOWED_HOSTS:", ALLOWED_HOSTS)
print("Using Production Settings")
