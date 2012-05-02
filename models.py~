from django.db import models
from django.contrib.auth.models import User

class ticket(models.Model):
    title = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
#    creator = models.ForeignKey(User)
    description = models.TextField()
    ranking = models.PositiveIntegerField()
#tags
    ### pictures ###
#    picture = models.ImageField()
    ### Geo Stuff ###
#    aprox_address = models.TextField()
#    zip_code = models.PositiveIntegerField()
#    coordinates = models.TextField()
    ### Gov stuff ###
#    jurisdiction = models.TextField()
#    official_recognition = models.BooleanField()
#    bid = models.PositiveIntegerField()
#    solved = models.BooleanField()

    def __unicode__(self):
        return self.title
