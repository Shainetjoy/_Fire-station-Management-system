from django.shortcuts import render, redirect
from fsApp.models import Guest, incident, Persons, Event, Resources, preAllocate
from .forms import Incident_register, AddnewPerson, AddEvent, AddResourceForm
from django.contrib import messages


def viewGuest(request):
    GustsDtl = Guest.objects.all()
    return render(request, 'admin/ViewGuests.html', {'GustsDtl': GustsDtl})


def deleteGuest(request, user_id):
    data = Guest.objects.get(user_id=user_id)
    data.delete()
    return redirect('viewGuest')


def incidentReg(request):
    incidentREgistrstionForm = Incident_register()
    if request.method == 'POST':
        incidentREgistrstionForm = Incident_register(request.POST, request.FILES)
        print(incidentREgistrstionForm, "rrrrrrrrrrrrr")
        if incidentREgistrstionForm.is_valid():
            incidentREgistrstionForm.save()
            return redirect('viewIncident')
    return render(request, 'admin/incidentRegister.html', {'incidentREgistrstionForm': incidentREgistrstionForm})


def viewIncident(request):
    allIncident = incident.objects.all()
    return render(request, 'admin/viewIncident.html', {'allIncident': allIncident})


def deleteIncident(request, id):
    data = incident.objects.get(id=id)
    data.delete()
    return redirect('viewIncident')


def updateIncident(request, id):
    upIncident = incident.objects.get(id=id)
    incidentREgistrstionForm = Incident_register(instance=upIncident)
    if request.method == 'POST':
        incidentREgistrstionForm = Incident_register(request.POST, instance=upIncident)
        if incidentREgistrstionForm.is_valid():
            incidentREgistrstionForm.save()
            return redirect('viewIncident')
    return render(request, 'admin/updateincident.html', {'incidentREgistrstionForm': incidentREgistrstionForm})


# def allowcationBtn1(request):
#     messages.success(request, 'personal Resource Allocated Successfully')
#     return render(request, 'admin/resourceAllocation.html')
#
#
# def allowcationBtn2(request):
#     messages.success(request, 'Equipment Resource Allocated Successfully')
#     return render(request, 'admin/resourceAllocation.html')
#
#
# def allowcationBtn3(request):
#     messages.success(request, 'Vehicles Resource Allocated Successfully')
#     return render(request, 'admin/resourceAllocation.html')
#

def Personsfun(request):
    return render(request, 'admin/person.html')


def viewPerson(request):
    allPersons = Persons.objects.all()
    return render(request, 'admin/viewAllPersons.html', {'allPersons': allPersons})


def deletePerson(request, id):
    data = Persons.objects.get(id=id)
    data.delete()
    return redirect('viewPerson')


def UpdatePerson(request, id):
    updatePerson = Persons.objects.get(id=id)
    AddPersonForm = AddnewPerson(instance=updatePerson)
    if request.method == 'POST':
        AddPersonForm = AddnewPerson(request.POST, instance=updatePerson)
        if AddPersonForm.is_valid():
            AddPersonForm.save()
            return redirect('viewPerson')
    return render(request, 'admin/updateperson.html', {'AddPersonForm': AddPersonForm})


def Maintenance(request):
    return render(request, 'admin/Maintenance-main.html')


# def AddequipmentFun(request):
#     addEqupmentForm = AddequipmentForm()
#     if request.method == 'POST':
#         addEqupmentForm = AddequipmentForm(request.POST)
#         if addEqupmentForm.is_valid():
#             addEqupmentForm.save()
#             return redirect('Maintenance')
#     return render(request,'admin/AddequipmentPage.html',{"addEqupmentForm":addEqupmentForm})


# def viewEquipment(request):
#     allEqupements = Addequipment.objects.all()
#     return render(request, 'admin/viewallEqupements.html', {'allEqupements': allEqupements})
#
# def deleteequipment(request , id):
#     data = Addequipment.objects.get(id=id)
#     data.delete()
#     return redirect('viewEquipment')
#
# def UpdateEquipments(request ,id):
#     eqpUpdate = Addequipment.objects.get(id=id)
#     addEqupmentForm = AddequipmentForm(instance=eqpUpdate)
#     if request.method == 'POST':
#         addEqupmentForm = AddequipmentForm(request.POST,instance=eqpUpdate)
#         if addEqupmentForm.is_valid():
#             addEqupmentForm.save()
#             return redirect('viewEquipment')
#     return render(request,"admin/updateResources.html",{'addEqupmentForm':addEqupmentForm})
#
#
#

def approveGuest(request, id):
    guest = Guest.objects.get(user_id=id)
    guest.approval_status = 1
    guest.save()
    messages.info(request, "Guest approved successfully")
    return redirect("viewGuest")


def approvePerson(request, id):
    person = Persons.objects.get(user_id=id)
    person.approval_status = 1
    person.save()
    messages.info(request, "Person approved successfully")
    return redirect("viewPerson")


def deleteEvents(request, id):
    data = Event.objects.get(id=id)
    data.delete()
    return redirect('viewEvents')


def viewEvents(request):
    eventDtl = Event.objects.all()
    return render(request, 'admin/ViewEvent.html', {'eventDtl': eventDtl})


def Add_Resources(request):
    form = AddResourceForm()
    if request.method == 'POST':
        form = AddResourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Resources addedd successfully')
            return redirect('view_resources')
    return render(request, 'admin/Add_Resources.html', {'form': form})


def view_resources(request):
    data = Resources.objects.all()
    return render(request, 'admin/view_resources.html', {'data': data})


def delete_resources(request, id):
    data = Resources.objects.get(id=id)
    data.delete()
    return redirect('view_resources')


def update_resources(request, id):
    all_resources = Resources.objects.get(id=id)
    updateForm = AddResourceForm(instance=all_resources)
    if request.method == 'POST':
        updateForm = AddResourceForm(request.POST, instance=all_resources)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('view_resources')
    return render(request, 'admin/updateResources.html', {"updateForm": updateForm})


# def addVehicle(request):
#     addVehicleForm = AddVehicle()
#     if request.method == 'POST':
#         addVehicleForm = AddVehicle(request.POST)
#         if addVehicleForm.is_valid():
#             addVehicleForm.save()
#             return redirect('viewVehicle')
#     return render(request,'admin/addVehicle.html',{"addVehicleForm":addVehicleForm})
#
#
# def viewVehicle(request):
#     EmrRequest = Vehicle_resources.objects.all()
#     return render(request,"admin/viewVehicle.html", {"EmrRequest": EmrRequest})
#
# def UpdateVehicle(request ,id):
#     eqpUpdate = Addequipment.objects.get(id=id)
#     addVehicleForm = AddequipmentForm(instance=eqpUpdate)
#     if request.method == 'POST':
#         addVehicleForm = AddequipmentForm(request.POST,instance=eqpUpdate)
#         if addVehicleForm.is_valid():
#             addVehicleForm.save()
#             return redirect('viewEquipment')
#     return render(request,"admin/updateVehicle.html",{'addVehicleForm':addVehicleForm})


def reportView(request):
    IncidentReport = incident.objects.all().order_by('-Date_and_Time_of_Incident')
    return render(request, "admin/reportView.html",{"IncidentReport":IncidentReport})


def preAllocating(request):
    personResource = Persons.objects.all().values('Name')
    allResources = Resources.objects.all().values('EquipmentName', 'EquipmentID', 'Vehicle_number','Vehicle_Name')
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
        preAllocate.objects.create(Employee=P_Resource,Vehicle = V_Resource,Equipment= E_Resource)
        return redirect('view_preAllocating')
    return render(request, 'admin/preAllocating.html', {'personResourceList': personResourceList,'equipment_names':equipment_names,'vehicle_name':vehicle_name})


def view_preAllocating(request):
    all_alowcations = preAllocate.objects.all()
    return render(request,"admin/viewpreAllocate.html",{"all_alowcations":all_alowcations})



def delete_PreAlocation(request, id):
    data = preAllocate.objects.get(id=id)
    data.delete()
    return redirect('view_preAllocating')
