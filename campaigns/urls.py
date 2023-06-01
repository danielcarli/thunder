from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:communication_id>/", views.communications, name="communication_details"),
    path("<int:communication_id/edit/",views.communication_edit, name="communication_edit"),
    path("<int:communication_id/milestone",views.communication_edit),
    path("<int:communication_id/task/",views.communication_edit),
    
]
