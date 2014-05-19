import json
from django.http import HttpResponse, HttpResponseRedirect


def vote(request):
    myvalue = request.POST.get("myvalue", "")
    results = int(myvalue) * 25
    reply = json.dumps(results)
    return HttpResponse(reply, mimetype='application/json')

def broken(request):
    results = {'success':False}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'vote'):
            pk = int(GET[u'pk'])
            vote = GET[u'vote']
            poll = Poll.objects.get(pk=pk)
            if vote == u"up":
                poll.up()
            elif vote == u"down":
                poll.down()
            results = {'success':True}
    reply = json.dumps(results)
    return HttpResponse(reply, mimetype='application/json')
