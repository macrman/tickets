from tickets.models import ticket
from django.forms.models import modelformset_factory
from django import forms
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

def index(request):
    ticket_index = ticket.objects.all().order_by('date_created')[:5]
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

def create_ticket(request):
    TicketFormSet = modelformset_factory(ticket)
    if request.method == 'POST':
        formset = TicketFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = TicketFormSet()
    return render_to_response("create_ticket.html", {
        "formset": formset,
    })
        #urls
#def edit_ticket(request):







