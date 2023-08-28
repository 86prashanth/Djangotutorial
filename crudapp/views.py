from django.shortcuts import render,redirect
from crudapp.forms import CrudRegistration,TeacherRegistration,StudentRegistration
from crudapp.models import Crudapp

# Create your views here.
def addshow(request):
    if request.method=='POST':
        fm=CrudRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=Crudapp(name=name,email=email,password=password)
            reg.save()
            fm=CrudRegistration()
    else:
        fm = CrudRegistration()  
    user=Crudapp.objects.all()  
    return render(request,'crud/addandshow.html',{'form':fm,'user':user})


def update(request,id):
    if request.method=='POST':
        pi=Crudapp.objects.get(pk=id)
        fm=CrudRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addshow')
    else:
        pi=Crudapp.objects.get(pk=id)
        fm=CrudRegistration(instance=pi)
    return render(request,'crud/update.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=Crudapp.objects.get(pk=id)
        pi.delete()
        return redirect('addshow')
 
   
def teacher_form(request):
    if request.method=='POST':
        fm=TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=TeacherRegistration()
    else:
        fm=TeacherRegistration()
    return render(request,'crud/teacher.html',{'form':fm})

def user_form(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    return render(request,'crud/userreg.html',{'form':fm})