from django.views import generic
from braces.views import LoginRequiredMixin
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.models.post import Post
from forum.forms import ThreadForm


class ThreadDetail(generic.TemplateView):
    template_name = 'forum/thread_detail.html'
        
    def get_context_data(self, **kwargs):
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        self.object = Thread.objects.get(
            forum=Forum.objects.get(forum_slug=self.kwargs['forum_slug']),
            thread_slug=self.kwargs['thread_slug'])
        context['thread'] = self.object
        context['thread_posts'] = Post.objects.filter(
            thread = self.object)
        return context    


class ThreadList(generic.ListView):
    model = Thread
    paginate_by = 25
    

class ThreadCreate(LoginRequiredMixin, generic.CreateView):
    model = Thread
    form_class = ThreadForm
    
    def get_form_kwargs(self):
        kwargs = super(ThreadCreate, self).get_form_kwargs()
        kwargs['forum'] = Forum.objects.get(forum_slug=self.kwargs['forum_slug'])
        kwargs['user'] = self.request.user
        return kwargs        


class ThreadUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Thread
    form_class = ThreadForm
    # this will be tricky....

