from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^acc/', include('myproject.accounts.urls', namespace="acc")),
    url(r'^admin/', include(admin.site.urls)),
)

