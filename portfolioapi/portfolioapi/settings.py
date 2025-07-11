"""
Django settings for portfolioapi project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os
import cloudinary
from cloudinary import CloudinaryImage
from cloudinary_storage.storage import MediaCloudinaryStorage
load_dotenv()



import psycopg2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = "django-insecure-rph#gcn3f3+d!5nw3wt2@v06v&86z^p9#+xc6#zb6%)a79!3$h"

# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
# DEBUG = os.environ.get('DEBUG')

DEBUG = False




# SECURITY WARNING: don't run with debug turned on in production!
# if DEBUG:
#     ALLOWED_HOSTS = ['*']
# else:
#     ALLOWED_HOSTS = ['portfolio-backend-w2tk.onrender.com']
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(' ') if not DEBUG else []

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolioapi.urls'

CORS_ALLOW_ALL_ORIGINS = True


# CORS_ALLOWED_ORIGINS = [
#     "https://portfolio-frontend-x9yr.onrender.com"
#     
# ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


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
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolioapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Database configuration


# DATABASE_URL = os.getenv('DATABASE_URL')

# DATABASES = {
#     'default': dj_database_url.parse(DATABASE_URL)
# }

# PROD_DB = os.environ.get("DATABASE_URL") is not None

# if PROD_DB:
#     DATABASES = {
#         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'porfolio',
#             'USER': 'root',
#             'PASSWORD': '',
#             'HOST': 'localhost',
#             'PORT': '3306',
#             'OPTIONS': {
#                 'sql_mode': 'STRICT_TRANS_TABLES',
#             },
#         }
#     }

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'porfolio',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'sql_mode': 'STRICT_TRANS_TABLES',
            },
        }
    }

DATABASES["default"] = dj_database_url.parse("postgresql://portfolio_0y0t_user:nFAEw2eEbYk9cmsoAbA7JPO6dGtC3JkA@dpg-d0hmj9qdbo4c73dukgfg-a.oregon-postgres.render.com/portfolio_0y0t")

#print("DATABASES:", DATABASES)



# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL'),
#         conn_max_age=600,
#         engine='django.db.backends.postgresql',
#     )
# }




    








#configuration pour déployer sur render.com
# if DEBUG == False :
#     # DATABASE_URL = "postgresql://portfolio_cx9f_user:PrtRKKM01eU99hU59zGqJwtkHcpdTEo6@dpg-cvpqhthr0fns73860qk0-a.oregon-postgres.render.com/portfolio_cx9f"
#     DATABASE_URL = "postgresql://portfolio_bdd_x8hx_user:5iK0qK18dCfSYtRD7mMLDn0el3j8Zi6v@dpg-d0greojuibrs73ftdr70-a.oregon-postgres.render.com/portfolio_bdd_x8hx"
   
#     DATABASES = {
#     'default': dj_database_url.config(
#         default = DATABASE_URL,
#         engine = 'django.db.backends.postgresql'
#     )
# }
    

# DATABASES = {
#     'default': dj_database_url.config(
#         default = os.getenv('DATABASE_URL'),     
#         engine = 'django.db.backends.postgresql',
#     )
# }


# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv("DATABASE_ENGINE"),
#         'NAME': os.getenv("DATABASE_NAME"),
#         'USER': os.getenv("DATABASE_USER"),
#         'PASSWORD': os.getenv("DATABASE_PASSWORD"),
#         'HOST': os.getenv("DATABASE_HOST"),
#         'PORT': os.getenv("DATABASE_PORT"),
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(default=DATABASE_URL)
# }




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# if DEBUG == False :
#     DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# else :
#     MEDIA_ROOT = BASE_DIR / 'media'
    

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_API_KEY"),
    'API_SECRET': os.getenv("CLOUDINARY_API_SECRET")
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-portfolio-cache',
    }
}


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR / 'django-error.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }


