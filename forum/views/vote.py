import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from forum.models.repute import PostVote
from forum.models.post import Post


@login_required
def vote(request):
    """
    allows a user to vote once.
    """
    vote = request.POST.get("vote", "")
    post_id = request.POST.get("id", "")

    u = request.user
    p = Post.objects.get(post_id=post_id)
    if vote == "up":
        v=1
    elif vote == "down":
        v=-1

    try: # update a vote, otherwise, create it.
        pv = PostVote(vote=1,
                      voted_at=datetime.now(),
                      user=u,
                      voted_post=p,)
        pv.save()
        status = "success"
    except:
        status = "fail"

    results = "%s, %s, %s, %s" % (vote, post_id, u, status)
    reply = json.dumps(results)
    return HttpResponse(reply, mimetype='application/json')

