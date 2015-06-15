# multilanguage
How to translate models of django app

# Installation

######First we need to install django-modeltranlation for this we need to put this command in shell


```
  pip install django-modeltranslation
```

# Configure settings file 

######Add modeltranslation to our installed apps

```
INSTALLED_APPS = (
    ...
    'modeltranslation',
    ....
  )
```

######Specify the traductions that we need and our local language code
    
  ```
    LANGUAGE_CODE = 'es'

    gettext = lambda s: s

    LANGUAGES = (
      ('es',  gettext('Spanish')),
      ('zh',  gettext('Chinese')),
      ('en',  gettext('English')),
    ) 
    
  ```
   
######Define url for i18n
  
  ```
    url(r'^i18n/', include('django.conf.urls.i18n'))
    
  ```
# Tranlating models

######We need to create in our app a new file called translation.py inside of this file we need to import translator, TranslationOptions, the model that you need to translate after this we need to add the fields that we need 

```
from modeltranslation.translator import translator, TranslationOptions
from models import News

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

translator.register(News, NewsTranslationOptions)    
```


