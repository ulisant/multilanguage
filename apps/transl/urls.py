from django.conf.urls import include, url
from .views import Inicio

urlpatterns = [
	url(r'^$',Inicio.as_view(), name='inicio-list'),
]