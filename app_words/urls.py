from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url('generar', views.generar),
    url('limpiar', views.limpiar),
]