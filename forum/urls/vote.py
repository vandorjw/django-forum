from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns(
    '',
    url(r'^vote/$', 'forum.views.vote.vote', name="vote"),    
)
