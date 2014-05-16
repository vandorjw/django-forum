from django import forms
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.models.post import Post


class ForumForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, *args, **kwargs):
        instance = super(ForumForm, self).save(commit=False)
        instance.save()
        instance.moderators.add(self.user)
        return instance
 
    class Meta:
        model = Forum


class ThreadForm(forms.ModelForm):
    def __init__(self, forum, user, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.user = user
        self.forum = forum

    def save(self, *args, **kwargs):
        instance = super(ThreadForm, self).save(commit=False)
        instance.user = self.user
        instance.forum = self.forum
        instance.save(*args, **kwargs)
        return instance
    
    class Meta:
        model = Thread
        exclude = ('forum', 'user', )


class PostForm(forms.ModelForm):
    def __init__(self, thread, user, parent, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.user = user
        self.thread = thread
        self.parent = parent

    def save(self, *args, **kwargs):
        instance = super(PostForm, self).save(commit=False, *args, **kwargs)
        instance.user = self.user
        instance.thread = self.thread
        instance.parent = self.parent
        instance.save(*args, **kwargs)
        return instance
  
    class Meta:
        model = Post
        fields = ['text',]
