from django.contrib import admin
from forum.models import Forum, Thread, Post



class ThreadInline(admin.StackedInline):
    model = Thread
    extra = 3


class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'forum_slug',
    )
    inlines = [ThreadInline]


class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'forum',
        'user',
        'name',
        'thread_slug',
        'positive',
        'negative',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',
        'positive',
        'negative',
    )

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
