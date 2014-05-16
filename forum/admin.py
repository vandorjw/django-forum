from django.contrib import admin
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.models.post import Post
from forum.models.repute import PostVote, ThreadVote


class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'forum_slug',
    )


class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'forum',
        'user',
        'name',
        'thread_slug',
        'vote_up_count',
        'vote_down_count',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',
        'vote_up_count',
        'vote_down_count',
    )

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(PostVote)
admin.site.register(ThreadVote)
