from django.shortcuts import render, redirect
from .forms import GuestRegister, UserRegister, AddnewPerson
from django.contrib import messages, auth
from django.contrib.auth import login, logout

from .models import Guest, Persons


# Create your views here.
def index(request):
    return render(request, "fsIndex.html")


def fsSignIn(request):
    if request.method == 'POST':
        username = request.POST.get('first')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",username,password)
        if user is not None and user.is_staff:
            print(1)
            login(request, user)
            return redirect('fsAdminIndex')
        elif user is not None and user.is_Persons:
            print(2)
            if user.Person.approval_status == 1:
                login(request, user)
                return redirect('fsEmplIndex')
        elif user is not None and user.is_Guest:
            if user.Guest.approval_status == 1:
                login(request, user)
                return redirect('fsGuestIndex')
        else:
            messages.info(request, "You Are Not A Registered User ")
    return render(request, "fsSignIn.html")


def GuestReg(request):
    UserReg = UserRegister()
    GuestReg = GuestRegister()
    if request.method == 'POST':
        UserReg = UserRegister(request.POST)
        GuestReg = GuestRegister(request.POST)
        if UserReg.is_valid() and GuestReg.is_valid():
            user = UserReg.save(commit=False)
            user.is_Guest = True
            user.save()
            gust = GuestReg.save(commit=False)
            gust.user = user
            gust.save()
            messages.info(request, "Invalid credentials")
            return redirect('fsSignIn')
    return render(request, 'fsSignUp.html', {'UserReg': UserReg, "GuestReg": GuestReg})


def employeReg(request):
    userRegForm = UserRegister()
    employeRegForm = AddnewPerson()
    if request.method == 'POST':
        userRegForm = UserRegister(request.POST)
        employeRegForm = AddnewPerson(request.POST,request.FILES)
        if userRegForm.is_valid() and employeRegForm.is_valid():
            user = userRegForm.save(commit=False)
            user.is_Persons = True
            user.save()
            empl = employeRegForm.save(commit=False)
            empl.user = user
            empl.save()
            return redirect('fsSignIn')
    return render(request, 'PersonReg.html', {'userRegForm': userRegForm, 'employeRegForm': employeRegForm})


def fsAdminIndex(request):
    return render(request, 'fsAdminIndex.html')


def fsEmplIndex(request):
    u = request.user.id
    Emp = Persons.objects.filter(user__id=u).values()
    Emp_name = Emp[0]['Name']
    return render(request, 'fsEmplIndex.html',{'Emp_name':Emp_name})


def fsGuestIndex(request):
    u = request.user.id
    customer = Guest.objects.filter(user__id=u).values()
    customer_name = customer[0]['Name']
    return render(request, 'fsGuestIndex.html', {"customer_name": customer_name})


def log_out(request):
    logout(request)
    return redirect('fsIndex')


