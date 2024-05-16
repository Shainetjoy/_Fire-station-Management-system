from django.contrib import messages
from django.shortcuts import render, redirect

from fsApp.forms import AllocateForm
from fsApp.models import incident, Event, Persons, Resources, Allocate


def EmpviewIncident(request):
    allIncident = incident.objects.all()
    return render(request, 'emp/viewIncident.html', {'allIncident': allIncident})


def EmpviewEvents(request):
    eventDtl = Event.objects.all()
    return render(request, 'emp/ViewEvent.html', {'eventDtl': eventDtl})

def approve_event(request,id):
    ow = Event.objects.get(id=id)
    ow.Approval_status = True
    ow.save()
    messages.info(request, 'approved')
    return redirect('EmpviewEvents')



def resourceAllocation(request):
    data1 = Resources.objects.all()
    data2 = Persons.objects.all()
    context = {
        'data1':data1,
        'data2':data2
    }
    return render(request, 'emp/resourceAllocation.html',context)


def allocating(request):
    personResource = Persons.objects.all().values('Name')
    allResources = Resources.objects.all().values('EquipmentName','Vehicle_Name')
    equipment_names = []
    vehicle_name = []
    personResourceList=[]
    for i in personResource:
        personResourceList.append(i['Name'])
    for resource in allResources:
        equipment_names.append(resource['EquipmentName'])
        vehicle_name.append(resource['Vehicle_Name'])
    if request.method == 'POST':
        P_Resource = request.POST.get('Personal_Resource')
        E_Resource = request.POST.get('equipment_name')
        V_Resource = request.POST.get('vehicle_name')
        Allocate.objects.create(Employee=P_Resource,Vehicle = V_Resource,Equipment= E_Resource)
        return redirect('fsEmplIndex')
    return render(request, 'emp/allocating.html', {'personResourceList': personResourceList,'equipment_names':equipment_names,'vehicle_name':vehicle_name})





# def allocating(request):
#     form = AllocateForm()
#     if request.method == 'POST':
#         form = AllocateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Allocated successfully')
#             return redirect('EmpviewEvents')
#         else:
#             print(form.errors)
#
#     # Print queryset for debugging
#     print("Vehicle Name Choices:", Resources.objects.values_list('id', 'Vehicle_Name'))
#     print("Equipment Name Choices:", Resources.objects.values_list('id', 'EquipmentName'))
#
#     return render(request, 'emp/allocating.html', {'form': form})