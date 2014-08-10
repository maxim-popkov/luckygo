from django.conf.urls import patterns, url

from luckygo import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^search/$', views.search),
    url(r'^details/(?P<path_id>\d+)/$', views.details),
    url(r'^twitter/$', views.twitter),
    
    # url(r'^$', views.index, name='index')
)