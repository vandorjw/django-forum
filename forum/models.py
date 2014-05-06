from datetime import date, datetime, timedelta
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Forum(models.Model):
    name = models.CharField(unique=True, max_length=254)
    forum_slug = models.SlugField(unique=True, max_length=254, editable=False)
    description = models.TextField()
    created = models.DateField(blank=True, null=True, editable=False)
    modified = models.DateField(blank=True, null=True, editable=False)
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="moderators")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:forum_detail',
                       kwargs={'forum_slug': self.forum_slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
            self.forum_slug = slugify(self.name)
        self.modified = datetime.now()
        super(Forum, self).save(*args, **kwargs)


class Thread(models.Model):
    forum = models.ForeignKey(Forum, verbose_name='forum')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="user")    
    name = models.CharField(max_length=254)
    thread_slug = models.SlugField(max_length=254, editable=False)
    description = models.TextField()
    positive = models.SmallIntegerField(default=0, editable=False)
    negative = models.SmallIntegerField(default=0, editable=False)
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


class Post(MPTTModel):
    thread = models.ForeignKey(Thread, verbose_name='thread')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="user")
    parent = TreeForeignKey('self', blank=True, null=True, related_name="children")
    created = models.DateField(blank=True, null=True, editable=False)
    modified = models.DateField(blank=True, null=True, editable=False)
    post_id = models.CharField(unique=True, max_length=45, editable=False)
    text = models.TextField()
    positive = models.SmallIntegerField(default=0, editable=False)
    negative = models.SmallIntegerField(default=0, editable=False)
    
    class MPTTMeta:
            order_insertion_by = ['id']    

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