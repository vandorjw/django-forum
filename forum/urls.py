from django.conf.urls import patterns, url
from forum import views

urlpatterns = patterns(
    '',
    url( # Site Index
        regex=r'^$',
        view=views.Index.as_view(),
        name='index'
    ),
    url( # Creates a new forum
        regex=r'^create/$',
        view=views.ForumCreate.as_view(),
        name='forum_create'
    ),
    url( # Update a forum
        regex=r'^f/(?P<forum_slug>[-\w]+)/admin/$',
        view=views.ForumUpdate.as_view(),
        name='forum_update'
    ),
    url( # View a forum
        regex=r'^f/(?P<forum_slug>[-\w]+)/$',
        view=views.ForumDetail.as_view(),
        name='forum_detail'
    ),
    url( # Create a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/create/$',
        view=views.ThreadCreate.as_view(),
        name="result_list"
    ),
    url( # link to a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/$',
        view=views.ThreadDetail.as_view(),
        name="thread_detail"
    ),
    url( # link to a post
        regex=r'^p/(?P<post_id>[-\w]+)/$',
        view=views.PostDetail.as_view(),
        name="post_detail"
    ),    
)
