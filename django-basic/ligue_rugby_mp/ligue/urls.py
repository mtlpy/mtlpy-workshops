from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ligue.views',
    url(r'^equipes/(?P<id>\d+)$', 'equipe_detail', name="equipe"),
)
