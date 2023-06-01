from django.db import models
from django.contrib.auth.models import User
class Team(models.Model):
    name = models.CharField(max_length=250)
    creation_date = models.DateTimeField("Team creation date", auto_now=True)
    users = models.ManyToManyField(User, null=True)
    def __str__(self) -> str:
        return self.name


