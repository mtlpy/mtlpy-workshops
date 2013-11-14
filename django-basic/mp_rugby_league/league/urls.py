# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('league.views',
    # team
    url(r'^teams$', 'team_list', name="teams"),
    url(r'^teams/(?P<id>\d+)$', 'team_detail', name="team"),

    # players
    url(r'^players$', 'player_list', name="players"),
    url(r'^players/(?P<id>\d+)$', 'player_detail', name="player"),
)
