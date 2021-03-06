# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    #url(r'^$', 'hackaway.views.home', name='home'),

    url(r'^articles/', include('hackaway.article.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^internal/search/(\w+)$', 'article.internal.search'),
    url(r'^internal/translate/(\w+)/(\w+)$', 'article.internal.translate'),
    url(r'^internal/languages$', 'article.internal.languages'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Static files
    url(r'^static/(?P<path>.*)$', serve,
        kwargs={'document_root':settings.STATIC_ROOT})
)
