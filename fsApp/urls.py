from django.urls import path
from fsApp import views, Adminviews, GuestView, EmpView

urlpatterns = [
path('',views.index,name='fsIndex'),
path('fsSignIn',views.fsSignIn,name='fsSignIn'),
path('GuestReg',views.GuestReg,name='GuestReg'),
path('log_out',views.log_out,name='log_out'),
path('fsAdminIndex',views.fsAdminIndex,name='fsAdminIndex'),
path('fsGuestIndex',views.fsGuestIndex,name='fsGuestIndex'),
path('fsEmplIndex',views.fsEmplIndex,name='fsEmplIndex'),
path('viewGuest',Adminviews.viewGuest,name='viewGuest'),
path('incidentRegister',Adminviews.incidentReg,name='incidentRegister'),
path('viewIncident',Adminviews.viewIncident,name='viewIncident'),
path('deleteIncident<int:id>',Adminviews.deleteIncident,name='deleteIncident'),
path('updateIncident<int:id>',Adminviews.updateIncident,name='updateIncident'),
# path('allowcationBtn1',Adminviews.allowcationBtn1,name='allowcationBtn1'),
# path('allowcationBtn2',Adminviews.allowcationBtn2,name='allowcationBtn2'),
# path('allowcationBtn3',Adminviews.allowcationBtn3,name='allowcationBtn3'),
path('Personsfun',Adminviews.Personsfun,name='Personsfun'),
path('viewEvents',Adminviews.viewEvents,name='viewEvents'),
path('viewPerson',Adminviews.viewPerson,name='viewPerson'),
path('employeReg',views.employeReg,name='employeReg'),
path('deletePerson/<int:id>/',Adminviews.deletePerson,name='deletePerson'),
path('UpdatePerson/<int:id>/',Adminviews.UpdatePerson,name='UpdatePerson'),
path('deleteGuest/<int:user_id>/',Adminviews.deleteGuest,name='deleteGuest'),
# path('deleteequipment/<int:id>/',Adminviews.deleteequipment,name='deleteequipment'),
path('deleteEvents/<int:id>/',Adminviews.deleteEvents,name='deleteEvents'),
path('Maintenance',Adminviews.Maintenance,name='Maintenance'),
# path('Addequipment',Adminviews.AddequipmentFun,name='Addequipment'),
# path('viewEquipment',Adminviews.viewEquipment,name='viewEquipment'),
path('guestviewIncident',GuestView.guestviewIncident,name='guestviewIncident'),
path('addEvent',GuestView.addEvent,name='addEvent'),
path('ViewMyEvents',GuestView.ViewMyEvents,name='ViewMyEvents'),

path('Add_Resources',Adminviews.Add_Resources,name='Add_Resources'),
path('view_resources',Adminviews.view_resources,name='view_resources'),
path('delete_resources/<int:id>',Adminviews.delete_resources,name='delete_resources'),
path('update_resources/<int:id>/',Adminviews.update_resources,name='update_resources'),




path('EmpviewEvents',EmpView.EmpviewEvents,name='EmpviewEvents'),
path('approve_event/<int:id>/',EmpView.approve_event,name='approve_event'),
path('approveGuest/<int:id>',Adminviews.approveGuest,name='approveGuest'),
path('approvePerson/<int:id>',Adminviews.approvePerson,name='approvePerson'),
# path('addVehicle',Adminviews.addVehicle,name='addVehicle'),
# path('viewVehicle',Adminviews.viewVehicle,name='viewVehicle'),
# path('UpdateVehicle/<int:id>',Adminviews.UpdateVehicle,name='UpdateVehicle'),
path('reportView',Adminviews.reportView,name='reportView'),
path('preAllocating',Adminviews.preAllocating,name='preAllocating'),
path('view_preAllocating',Adminviews.view_preAllocating,name='view_preAllocating'),
path('delete_PreAlocation/<int:id>',Adminviews.delete_PreAlocation,name='delete_PreAlocation'),



path('EmpviewIncident',EmpView.EmpviewIncident,name='EmpviewIncident'),
path('EmpviewEvents',EmpView.EmpviewEvents,name='EmpviewEvents'),
path('resourceAllocation',EmpView.resourceAllocation,name='resourceAllocation'),
path('allocating',EmpView.allocating,name='allocating'),



]