from django.conf.urls import patterns, include, url
from forum.views import forum

urlpatterns = patterns(
    '',
    url( # Creates a new forum
        regex=r'^create/$',
        view=forum.ForumCreate.as_view(),
        name='forum_create'
    ),
    url( # Update a forum
        regex=r'^f/(?P<forum_slug>[-\w]+)/admin/$',
        view=forum.ForumUpdate.as_view(),
        name='forum_update'
    ),
    url( # View a forum
        regex=r'^f/(?P<forum_slug>[-\w]+)/$',
        view=forum.ForumDetail.as_view(),
        name='forum_detail'
    ),   
)
