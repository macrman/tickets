from tickets.models import ticket, ticket_form
from django.views.generic import list_detail, create_update
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
    if request.method == 'POST':
        form = ticket_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ticket_form()

    return render_to_response('create_ticket.html', {
        'form': form,
    })
def edit_ticket(request):
    return "hello world"






