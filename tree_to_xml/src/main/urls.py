__author__ = 'alex'
# -*- coding: utf-8 -*-


from django.conf.urls import url, patterns

urlpatterns = patterns('tree_to_xml.src.main.views',
    url(r'^create/?$', 'create'),
    url(r'^get_all/?$', 'get_all'),
    url(r'^update/?$', 'update'),
    url(r'^delete/?$', 'delete'),
    url(r'^get_xml/?$', 'get_xml'),
    url(r'^$', 'index'),
)

