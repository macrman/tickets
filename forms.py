from django.forms import ModelForm
from tickets.models import ticket

class ticket_form(ModelForm):
    class Meta:
        model = ticket
        fields = ('title','description',)
