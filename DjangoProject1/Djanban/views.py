from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import json

from Djanban.models import WorkItem

#start page
def index(request):
    return render(request, 'Board/index.html')

# the board
def board(request, team_id):
    def Team(id):
        return {
            '0': 'Team Blue',
            '1': 'Team Red',
            '3': 'Team Green',
            '4': 'Team Orange'
        }[id]
 #data to the board
    return render(request, 'Board/detail.html', {
            'teamid': team_id,
            'team': Team(team_id)
            })

def items(request, team_id):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")
    

# om vi har objekt
#tasks = Task.objects.all()
#data = serializers.serialize("json", tasks)
#return HttpResponse(data, content_type='application/json')
 
#def vote(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the poll voting form.
#        return render(request, 'polls/detail.html', {
#            'poll': p,
#            'error_message': "You didn't select a choice.",
#    })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
