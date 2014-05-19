from django.views import generic
from forum.models.forum import Forum


class Index(generic.TemplateView):
    template_name = 'forum/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['forums'] = Forum.objects.all()
        return context
