from . import views
from django.urls import path
urlpatterns = [
    path('employee',views.employeeform,name='employee'),
    path('Add_employee',views.add_employee,name="employeeadded"),
    path('',views.display,name='dashboard'),
    path('editemployee/<eid>',views.edit,name='editemployeee'),
    path('deleteemployee/<eid>',views.delete,name='deleteemployeee'),
]
