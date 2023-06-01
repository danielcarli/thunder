from django.contrib import admin
from campaigns.models import CommunicationDemand, CommunicationType, TaskGroup, Task
# Register your models here.
admin.site.register(CommunicationDemand)
admin.site.register(CommunicationType)
admin.site.register(TaskGroup)
admin.site.register(Task)