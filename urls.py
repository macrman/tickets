from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, CreateView
from tickets.models import ticket
from tickets.forms import ticket_form
from tickets.views import ticket_detail, ticket_list, ticket_create

urlpatterns = patterns('',
    (r'^$',
        ticket_list.as_view()),
    (r'^(?P<pk>\d+)/$',
        ticket_detail.as_view()),
    (r'^create/$',
        ticket_create.as_view()),
)

#edit_ticket

