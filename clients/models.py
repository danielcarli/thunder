from django.db import models
from teams.models import Team

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    creation_date = models.DateTimeField("Cliente creation Date", auto_now=True)
    #team_owner = models.ForeignKey(Team)

    def __str__(self) -> str:
        return self.name