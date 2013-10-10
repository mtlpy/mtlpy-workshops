# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # lrmp
    url(r'^$', 'ligue_rugby_mp.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        dict(template_name='connexion.html',), 
        'connexion'
    ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
        dict(template_name='deconnexion.html',), 
        'deconnexion'
    ),
    url(r'^admin/', include(admin.site.urls)),

    # équipes
    url(r'^', include('ligue.urls')),
)

urlpatterns += staticfiles_urlpatterns()
