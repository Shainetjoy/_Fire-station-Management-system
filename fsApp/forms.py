from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from fsApp.models import Guest, User, incident, Persons, Event, Event_contestents, Resources, Allocate


class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='conform password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password1','password2')


class GuestRegister(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ("user","approval_status")


class Incident_register(forms.ModelForm):
    class Meta:
        model = incident
        fields = '__all__'


class AddnewPerson(forms.ModelForm):
    # hire_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Persons
        exclude = ("user","approval_status",)


class AddResourceForm(forms.ModelForm):
    Purchase_Date=forms.DateField(widget=DateInput)
    Last_Maintenance_Date=forms.DateField(widget=DateInput)
    Next_Maintenance_Due=forms.DateField(widget=DateInput)
    Maintenance_Schedule=forms.DateField(widget=DateInput)
    Next_Inspection_Date=forms.DateField(widget=DateInput)

    class Meta:
        model = Resources
        fields =  '__all__'


class AddEvent(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    class Meta:
        model = Event
        exclude = ('user','Approval_status')



class Event_contestentsForm(forms.ModelForm):
    class Meta:
        model = Event_contestents
        fields = '__all__'


# class EmergenyIncidentForm(forms.ModelForm):
#     Date = forms.DateField(widget=DateInput)
#     class Meta :
#         model = EmergencyRequest
#         exclude = ("Time",)

class AllocateForm(forms.ModelForm):
    class Meta:
        model = Allocate
        fields = '__all__'
