from datetime import date, datetime, timedelta
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from forum.models.post import Post
from forum.models.thread import Thread


class VoteManager(models.Manager):
    def get_up_vote_count_from_user(self, user):
        if user is not None:
            return self.filter(user=user, vote=1).count()
        else:
            return 0

    def get_down_vote_count_from_user(self, user):
        if user is not None:
            return self.filter(user=user, vote=-1).count()
        else:
            return 0

    def get_votes_count_today_from_user(self, user):
        if user is not None:
            today = date.today()
            return self.filter(user=user, voted_at__range=(
                today, today + timedelta(1))).count()
        else:
            return 0


class Vote(models.Model):
    VOTE_UP = +1
    VOTE_DOWN = -1
    VOTE_CHOICES = (
        (VOTE_UP, 'Up'),
        (VOTE_DOWN, 'Down'),
    )
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
    voted_at = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

    def __str__(self):
        return '[%s] voted at %s: %s' %(self.user, self.voted_at, self.vote)

    def is_upvote(self):
        return self.vote == self.VOTE_UP

    def is_downvote(self):
        return self.vote == self.VOTE_DOWN


class PostVote(Vote):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_votes')
    voted_post = models.ForeignKey(Post, related_name='post_votes')

    repute = VoteManager()

    class Meta:
        unique_together = ('user', 'voted_post')
        app_label = 'forum'


class ThreadVote(Vote):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='thread_votes')
    voted_thread = models.ForeignKey(Thread, related_name='thread_votes')

    repute = VoteManager()

    class Meta:
        unique_together = ('user', 'voted_thread')
        app_label = 'forum'
