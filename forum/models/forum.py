from datetime import datetime
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Forum(models.Model):
    name = models.CharField(
        unique=True,
        max_length=254
    )

    forum_slug = models.SlugField(
        unique=True,
        max_length=254,
        editable=False,
    )
    description = models.TextField()

    created = models.DateField(
        blank=True,
        null=True,
        editable=False,
    )

    modified = models.DateField(
        blank=True,
        null=True,
        editable=False,
    )

    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="moderators",
    )

    class Meta:
        app_label = 'forum'

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
