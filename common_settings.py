import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-database',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '9996',
    }
}

WIFI_API_KEY = 'your-wifi-api-key'
SECRET_PASSWORD = 'your-secret-password'

# Example distance control setting
MAX_DISTANCE = 8192