from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class ticket(models.Model):
    title = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ranking = models.PositiveIntegerField(default=0)

#    tags
#    creator = models.ForeignKey(User)
#    picture = models.ImageField()
#    aprox_address = models.TextField()
#    zip_code = models.PositiveIntegerField()
#    coordinates = models.TextField()
#    jurisdiction = models.TextField()
#    official_recognition = models.BooleanField()
#    bid = models.PositiveIntegerField()
#    is_fixed = models.BooleanField()

    def __unicode__(self):
        return self.title


