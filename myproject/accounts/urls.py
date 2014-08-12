from django.conf.urls import patterns, url
from myproject.accounts import views

urlpatterns = patterns('',
    url(r'^create$', views.create),
    url(r'^$', views.index, name='index')
)
