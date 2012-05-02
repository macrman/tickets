from django.conf.urls import patterns, include, url
from tickets.views import *

urlpatterns = patterns('tickets.views',
    url(r'^$',
        'index'),
<<<<<<< HEAD
    url(r'^create/$',
        'create_ticket'),
    url(r'^(?P<ticket_id>\d+)/$',
        'view_ticket'),
    url(r'^(?P<ticket_id>\d+)/edit/$',
        'edit_ticket'),
    )
=======
    url(r'^add/$',
        'add_ticket'),
    url(r'^(?P<ticket_id>\d+)/$',
        'view_ticket'),
#    url(r'^(?P<ticket_id>\d+)/edit/$',
 #       'edit_ticket'),
)
>>>>>>> master
