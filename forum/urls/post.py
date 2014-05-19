from django.conf.urls import patterns, url
from forum.views import post

urlpatterns = patterns(
    '',
    url( # create a post
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/reply/$',
        view=post.PostCreate.as_view(),
        name="thread_reply"
    ),     
    url( # create a post
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/(?P<post_id>[-\w]+)/reply/$',
        view=post.PostCreate.as_view(),
        name="post_reply"
    ),     
    url( # link to a post
        regex=r'^p/(?P<post_id>[-\w]+)/$',
        view=post.PostDetail.as_view(),
        name="post_detail"
    ),
    url( # edit a post
        regex=r'^p/(?P<post_id>[-\w]+)/update/$',
        view=post.PostUpdate.as_view(),
        name="post_update"
    ),    
)
