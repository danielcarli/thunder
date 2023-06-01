from django.db import models
from clients.models import Client
from django.contrib.auth.models import User
from teams.models import Team
# Create your models here.


class CommunicationType(models.Model):
    name = models.CharField(max_length=250)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    color = models.CharField(max_length=20,default="#999999")
    
    def __str__(self) -> str:
        return self.name

class CommunicationDemand(models.Model):
    STATUS = [
        ("CANCELED", "Canceled"),
        ("DONE", "Done"),
        ("WAITING", "Waiting to Start"),
        ("NEW", "New"),
        ("DOING", "Executando"),
        ('TEMPLATE', "Template Model")
    ]
    ORGANIZATION_STRATEGY = [
        ('HIGHT','Alta'),
        ('MEDIUM','Média'),
        ('LOW','Baixa'),
        ('UNDEFINED','Não definida')
    ]
    name = models.CharField(max_length=250)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    starts_in = models.DateTimeField("starts in",null=True, default=None)
    final_deadline = models.DateTimeField("Final deadline",null=True, default=None)
    general_drive_url = models.URLField(default="")
    deliverables_drive_url = models.URLField(default="")
    organization_strategy = models.CharField(max_length=10, choices=ORGANIZATION_STRATEGY, default='UNDEFINED')
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="NEW")
    type = models.ForeignKey(CommunicationType, null=True, on_delete=models.SET_NULL)
    owner = models.ManyToManyField(Team,null=True)
    managers = models.ManyToManyField(User,null=True)
    requester_name = models.CharField("Nome do solicitante", max_length=20, null=True)
    requester_email = models.EmailField("E-mail do solicitante", null=True, default=None )
    requester_whatsapp =  models.CharField("Whatsapp do solicitante", max_length=20, null=True, default="")
    
    def __str__(self) -> str:
        return self.name
   
class TaskGroup(models.Model):
    name = models.CharField(default="",max_length=250)
    deadline_date = models.DateTimeField()
    commmunication = models.ForeignKey(CommunicationDemand, on_delete=models.CASCADE)
    description = models.TextField()
    assigned  = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    name = models.CharField(default="", max_length=250)
    description = models.TextField()
    deadline_date = models.DateTimeField(null=True)
    task_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through="UserTaskStatus")
   
    def __str__(self):
        return self.name


class UserTaskStatus(models.Model):
    USER_TASK_STATUS = [
        ("CANCELED", "Canceled"),
        ("TO DO", "To do"),
        ("DOING", "Doing"),
        ("DONE", "Done")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    status = models.CharField(max_length=20, 
                              choices=USER_TASK_STATUS, 
                              default="TO DO")
    def __str__(self) -> str:
        return "%s - %s - %s", self.user, self.task, self.status  
   
     