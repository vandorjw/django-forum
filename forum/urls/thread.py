from django.conf.urls import patterns, url
from forum.views import thread

urlpatterns = patterns(
    '',
    url( # Create a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/create/$',
        view=thread.ThreadCreate.as_view(),
        name="thread_create"
    ),
    url( # Update a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/update/$',
        view=thread.ThreadUpdate.as_view(),
        name="thread_create"
    ),    
    url( # link to a thread
        regex=r'^f/(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/$',
        view=thread.ThreadDetail.as_view(),
        name="thread_detail"
    ),
)
