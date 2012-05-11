from django.conf.urls import patterns, include, url
from tickets.models import ticket
from tickets.forms import ticket_form
from tickets.views import ticket_list, ticket_detail, create_ticket
urlpatterns = patterns('',
    (r'^$',
        ticket_list.as_view()),
    (r'^(?P<pk>\d+)/$',
        ticket_detail.as_view()),
    (r'^create/$',
        create_ticket.as_view()),
    (r'^thanks/$',
        thanks_view.as_view()),
)

#edit_ticket

