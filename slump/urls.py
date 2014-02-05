# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from slump import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^history/$', views.history, name='history'),
)