from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns(
    '',
    url(
        regex=r'^$',
        view=views.Index.as_view(),
        name='index'
    ),
    url(r'^', include('forum.urls.forum')),
    url(r'^', include('forum.urls.thread')),
    url(r'^', include('forum.urls.post')),
    url(r'^', include('forum.urls.vote')),
)
