from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from tickets.models import ticket



urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
        model=ticket,
        template_name="index.html",
        context_object_name="ticket_list",)),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
        model = ticket,
        template_name="view_ticket.html",
        )),


)
