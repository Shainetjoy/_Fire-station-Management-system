from django.shortcuts import render, redirect
import datetime
from fsApp.forms import  AddEvent
from fsApp.models import incident, Guest, Event, Event_contestents


# def GustIncedentView(request):
#     gustInciddentView = incident.objects.fillter()
#     return render(request,'guest/GustincidentView.html')


def guestviewIncident(request):
    allIncident = incident.objects.all()
    # u = request.user.id
    # customer = Guest.objects.filter(user__id=u).values()
    # customer_name = customer[0]['Name']
    return render(request, 'guest/viewIncident.html', {'allIncident': allIncident})



def addEvent(request):
    u=request.user
    print(u)
    newEvent = AddEvent()
    if request.method == 'POST':
        newEvent = AddEvent(request.POST)
        if newEvent.is_valid():
            data = newEvent.save(commit=False)
            data.user = u
            data.save()
            return redirect('ViewMyEvents')
    return render(request,'guest/AddEvent.html',{"newEvent":newEvent})


def ViewMyEvents(request):
    myId = request.user
    allEvent = Event.objects.filter(user_id = myId)
    return render(request,'guest/ViewMyEvents.html',{"allEvent":allEvent})



# def GustIncedentView(request):
#     gustInciddentView = incident.objects.fillter()
#     return render(request,'guest/GustincidentView.html')





