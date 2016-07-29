from datetime import datetime
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from forum.models.forum import Forum


class Thread(models.Model):
    forum = models.ForeignKey(Forum, verbose_name='forum')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="user")    
    name = models.CharField(max_length=254)
    thread_slug = models.SlugField(max_length=254, editable=False)
    description = models.TextField()
    vote_up_count = models.IntegerField(default=0, editable=False)
    vote_down_count = models.IntegerField(default=0, editable=False)
    created = models.DateField(blank=True, null=True, editable=False)
    modified = models.DateField(blank=True, null=True, editable=False)
    
    class Meta:
        app_label = 'forum'
        unique_together = ('forum', 'thread_slug')    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:thread_detail',
                       kwargs={'thread_slug': self.thread_slug,
                               'forum_slug': self.forum.forum_slug,})

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
            yyyymmdd = self.created.strftime('%Y%m%d')
            self.thread_slug = yyyymmdd + "-" + slugify(self.name)
        self.modified = datetime.now()
        super(Thread, self).save(*args, **kwargs)
