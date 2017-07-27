MIDDLEWARE.append('api.middleware.dev_cors_middleware')

DEBUG = True
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django',
    'USER': 'django',
    'PASSWORD': '1234',
    'HOST': '',
    'PORT': '',
}
