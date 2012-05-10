from tickets.models import ticket
from tickets.forms import ticket_form
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render_to_response
from django.forms import ModelForm

class ticket_list(ListView):
    model = ticket
    template_name = "ticket_list.html"
    context_object_name = "ticket_list"

class ticket_detail(DetailView):
    model = ticket
    template_name = "ticket_detail.html"

#def create_ticket(request):
#    helloworld = "weee"
#    return render_to_response('create_ticket.html', {
#        'helloworld': helloworld })
class create_ticket(CreateView):
    model = ticket
    form_class = ticket_form
    template_name = "create_ticket.html"
    #redirect url


