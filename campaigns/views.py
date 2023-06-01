from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from campaigns.models import CommunicationDemand 

# Create your views here.
def index(request):
    communication_demand_list = CommunicationDemand.objects.order_by("-id")
    context = {
        'communication_demand_list': communication_demand_list,
    }
    return render(request, "communications/index.html", context)
    

def communications(request, communication_id):
    communicationDemand = get_object_or_404(CommunicationDemand, pk=communication_id)
    context = {
        'communicationDemand': communicationDemand
    }
    return render(request, "communications/communication_details.html",context)

def communication_edit(request, communication_id):
    return HttpResponse("Editing campaign %s." % communication_id)
