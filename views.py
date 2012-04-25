from tickets.models import ticket

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

def index(request):
    ticket_index = ticket.objects.all().order_by('created')[:5]
    t = loader.get_template('index.html')
    c = Context({
        'ticket_index': ticket_index,
    })
    return HttpResponse(t.render(c))
    
def view_ticket(request, ticket_id):
    try:
        t = ticket.objects.get(pk=ticket_id)
    except:
        raise Http404
    return render_to_response('view_ticket.html',
        {'ticket': t,
        'desc': t.description,})
        
#def edit_ticket(request):

#def add_ticket(request):
