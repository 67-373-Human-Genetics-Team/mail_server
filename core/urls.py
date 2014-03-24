from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^send$', views.sendMessage, name='send'),
    url(r'^sendRaw$', views.sendRawMessage, name='send'),
)
