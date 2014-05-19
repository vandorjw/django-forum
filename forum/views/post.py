from django.views import generic
from braces.views import LoginRequiredMixin
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.models.post import Post
from forum.forms import PostForm

class PostDetail(generic.DetailView):
    model = Post
    slug_field = 'post_id'
    slug_url_kwarg = 'post_id'


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    
    def get_form_kwargs(self):
        kwargs = super(PostCreate, self).get_form_kwargs()
        kwargs['thread'] = Thread.objects.get(
            forum=Forum.objects.get(forum_slug=self.kwargs['forum_slug']),
            thread_slug=self.kwargs['thread_slug'])
        kwargs['user'] = self.request.user
        if 'post_id' in self.kwargs:
            kwargs['parent'] = Post.objects.get(post_id=self.kwargs['post_id'])
        else:
            kwargs['parent'] = None
        return kwargs        


class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
