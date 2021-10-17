

import os
from pathlib import Path

from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


SECRET_KEY = 'django-insecure-fdn0y3@a#qz@-+6(k3dh%-yhv$(e5i=mri60v+k2k3p7(l(k+2'


DEBUG = True

ALLOWED_HOSTS = []
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'UserApp.backends.CaseInsensitiveModelBackend'
)



INSTALLED_APPS = [
  
    'adminlte3',
    
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'IBay',
    'Location',
    'Products',
    'Stores',
    'Marketing',
    'OrderApp',
    'UserApp',
    'rest_framework',
    'mptt',
    'crispy_forms',
    'widget_tweaks',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IBay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Stores.context_processors.categories',                
            ],
        },
    },
]

WSGI_APPLICATION = 'IBay.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT=os.environ.get('EMAIL_PORT')




MESSAGE_TAGS={
    messages.ERROR:'danger'
}


LOGIN_URL='login'
LOGIN_REDIRECT_URL='home'
LOGOUT_URL='logout'
LOGOUT_REDIRECT_URL='login'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'

MEDIA_ROOT = MEDIA_DIR


SITE_ID = 1
AUTH_USER_MODEL = 'UserApp.UserBase'



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

