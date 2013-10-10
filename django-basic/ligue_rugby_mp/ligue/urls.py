# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('ligue.views',
    # équipe
    url(r'^equipes$', 'equipe_list', name="equipes"),
    url(r'^equipes/(?P<id>\d+)$', 'equipe_detail', name="equipe"),

    # joueurs
    url(r'^joueurs$', 'joueur_list', name="joueurs"),
    url(r'^joueurs/(?P<id>\d+)$', 'joueur_detail', name="joueur"),
)
