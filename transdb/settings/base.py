from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '8t$0ywoy1kx#r0p*2s5y21^!xrzpcjdrbyg+2=mx7bilep=!)4'

# Application definition

DJANGO_APPS = (
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    )

THIRD_PARTY_APPS = (

    'modeltranslation',

    )

LOCAL_APPS = (

    'apps.transl',
    
    )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'transdb.urls'

WSGI_APPLICATION = 'transdb.wsgi.application'

gettext = lambda s: s

LANGUAGES = (
    ('es',  gettext('Spanish')),
    ('zh',  gettext('Chinese')),
    ('en',  gettext('English')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
