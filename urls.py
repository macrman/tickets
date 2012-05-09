from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, CreateView
from tickets.models import ticket
from tickets.forms import ticket_form

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
        model = ticket,
        template_name = "ticket_list.html",
        context_object_name = "ticket_list",
        )),

    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
        model = ticket,
        template_name = "ticket_detail.html",
        )),
    (r'^create/$',
        CreateView.as_view(
        model = ticket,
        form_class = ticket_form,
        template_name = "create_ticket.html",
        )),
)
