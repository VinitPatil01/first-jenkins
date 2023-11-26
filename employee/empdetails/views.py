from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import empdetails
# Create your views here.
def employeeform(request):
    return render(request,'add_employee.html')

def add_employee(request):
    if request.method=='POST':
        a=request.POST['ename']
        b=request.POST['emno']
        c=request.POST['emailadd']
        empdata=empdetails.objects.create(ename=a,emno=b,email=c)
        empdata.save()
    return redirect('/')
def display(request):
    content={}
    content['data']=empdetails.objects.all()
    return render(request,'dashboard.html',content)
def delete(request,eid):
    emp=empdetails.objects.get(id=eid)
    emp.delete()
    return redirect('/')
def edit(request,eid):
    if request.method=='POST':
        x=request.POST['ename']
        y=request.POST['emno']
        z=request.POST['emailadd']
        update_emp=empdetails.objects.filter(id=eid)
        update_emp.update(ename=x,emno=y,email=z)
        return redirect('/')
    else:
        content={}
        content['data']=empdetails.objects.get(id=eid)
        return render(request,'edit_employee.html',content)
