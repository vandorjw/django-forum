from forum.models import Forum

def forum_list(request):
    return {'forum_list': Forum.objects.all()}