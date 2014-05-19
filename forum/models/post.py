from datetime import datetime
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey

from forum.models.thread import Thread


class Post(MPTTModel):
    thread = models.ForeignKey(Thread, verbose_name='thread')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="user")
    parent = TreeForeignKey('self', blank=True, null=True, related_name="children")
    created = models.DateField(blank=True, null=True, editable=False)
    modified = models.DateField(blank=True, null=True, editable=False)
    post_id = models.CharField(unique=True, max_length=45, editable=False)
    text = models.TextField()
    vote_up_count = models.IntegerField(default=0, editable=False)
    vote_down_count = models.IntegerField(default=0, editable=False)

    class Meta:
        app_label = 'forum'
    
    def __str__(self):
        return self.post_id

    def get_absolute_url(self):
        return reverse('forum:post_detail', kwargs={'post_id': self.post_id})

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
            yyyymmdd = self.created.strftime('%Y%m%d')
            self.post_id = yyyymmdd + "-" + str(uuid4())
        self.modified = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def score(self):
        return "%s" % (self.vote_up_count - self.vote_down_count)
