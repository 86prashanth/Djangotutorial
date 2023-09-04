from django.shortcuts import render,redirect
from crudapp.forms import CrudRegistration,TeacherRegistration,StudentRegistration
from crudapp.models import Crudapp
from django.views.generic.base import TemplateView,RedirectView
from django.views import View 
# Create your views here.
class UserAddShowView(TemplateView):
    template_name='crudcbv/addandshow.html'
    # get data
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        form=CrudRegistration()
        user=Crudapp.objects.all()
        context={'form':form,'user':user}
        return context
    # post data
    def post(self,request):
        form=CrudRegistration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            pswd=form.cleaned_data['password']
            reg=Crudapp(name=name,email=email,password=pswd)
            reg.save()
        return redirect('addshow')
    
    
# function based view
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

# class based update view 
class UserUpdateView(View):
    # get data
    def get(self,request,id):
        user=Crudapp.objects.get(pk=id)
        form=CrudRegistration(instance=user)
        return render(request,'crudcbv/update_view.html',{'form':form})
    
    # post data 
    def post(self,request,id):
        user=Crudapp.objects.get(pk=id)
        form=StudentRegistration(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('addshow')
        # return render(request,'crudcbv/update_view.html',{'form':form})
        
        

# function based update view
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


# function based delete view
def delete_data(request,id):
    if request.method=='POST':
        pi=Crudapp.objects.get(pk=id)
        pi.delete()
        return redirect('addshow')
 
# class based delete view 
class UserDeleteView(RedirectView):
        url='addshow'
        def get_redirect_url(self,*args,**kwargs):
            print(kwargs)
            del_id=kwargs['id']
            Crudapp.objects.get(pk=del_id)
            return super().get_redirect_url(*args,**kwargs)
   
# teacher form
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