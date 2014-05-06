from django.views import generic
from braces.views import LoginRequiredMixin
from forum.models import Forum, Thread, Post
from forum.forms import ForumForm, ThreadForm, PostForm

class Index(generic.TemplateView):
    template_name = 'forum/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['forums'] = Forum.objects.all()
        return context     


class IndexHot(generic.TemplateView):
    template_name = 'forum/index.html'


class IndexTop(generic.TemplateView):
    template_name = 'forum/index.html'


class ForumDetail(generic.DetailView):
    model = Forum
    slug_field = 'forum_slug'
    slug_url_kwarg = 'forum_slug'


class ForumList(generic.ListView):
    model = Forum
    paginate_by = 25


class ForumCreate(LoginRequiredMixin, generic.CreateView):
    model = Forum
    form_class = ForumForm

    def get_form_kwargs(self):
        kwargs = super(ForumCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ForumUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Forum
    form_class = ForumForm
    slug_field = 'forum_slug'
    slug_url_kwarg = 'forum_slug'
    
    def get_form_kwargs(self):
        kwargs = super(ForumUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs    


class ThreadDetail(generic.TemplateView):
    template_name = 'forum/thread_detail.html'
        
    def get_context_data(self, **kwargs):
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        self.object = Thread.objects.get(
            forum=Forum.objects.get(forum_slug=self.kwargs['forum_slug']),
            thread_slug=self.kwargs['thread_slug'])
        context['thread'] = self.object
        context['root_posts'] = Post.objects.filter(
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


class PostDetail(generic.DetailView):
    model = Post
    slug_field = 'post_id'
    slug_url_kwarg = 'post_id'    