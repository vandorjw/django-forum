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
        name="thread_create"
    ),
    url( # Update a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/update/$',
        view=views.ThreadUpdate.as_view(),
        name="thread_create"
    ),    
    url( # link to a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/$',
        view=views.ThreadDetail.as_view(),
        name="thread_detail"
    ),
    url( # create a post
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/reply/$',
        view=views.PostCreate.as_view(),
        name="thread_reply"
    ),     
    url( # create a post
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/(?P<post_id>[-\w]+)/reply/$',
        view=views.PostCreate.as_view(),
        name="post_reply"
    ),     
    url( # link to a post
        regex=r'^p/(?P<post_id>[-\w]+)/$',
        view=views.PostDetail.as_view(),
        name="post_detail"
    ),
    url( # edit a post
        regex=r'^p/(?P<post_id>[-\w]+)/update/$',
        view=views.PostUpdate.as_view(),
        name="post_update"
    ),    
)
