from django.views import generic
from braces.views import LoginRequiredMixin
from forum.models.forum import Forum
from forum.forms import ForumForm


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
