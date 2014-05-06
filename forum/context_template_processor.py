from django.http import HttpResponse
from django.template import RequestContext

def all_forums(request):
    return {'ip_address': request.META['REMOTE_ADDR']}