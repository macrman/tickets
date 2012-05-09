from tickets.models import ticket
from tickets.forms import ticket_form
from django.views.generic import ListView, DetailView, CreateView

class ticket_list(ListView):
    model = ticket
    template_name = "ticket_list.html"
    context_object_name = "ticket_list"

class ticket_detail(DetailView):
    model = ticket
    template_name = "ticket_detail.html"

class ticket_create(CreateView):
    model = ticket
    form_class = ticket_form
    template_name = "create_ticket.html"
