from django.shortcuts import render,redirect
from formapp.forms import StudentRegistration,Registration,ModelRegistration
from django.http import HttpResponse
from formapp.models import User 


# Create your views here.
def showfromdata(request):
    # form=StudentRegistration(auto_id=True,label_suffix='',initial={'name':'username','email':'useremail'})
    form=StudentRegistration()
    form.order_fields(field_order=['email','name','firstname'])
    return render(request,'form/showinfo.html',{'form':form})

def ShowRegistration(request):
    if request.method=='POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            
            print("form validated")
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            # print("name:",fm.cleaned_data['name'])
            # print('email:',fm.cleaned_data['email'])
            # print('password:',fm.cleaned_data['password'])
            # reg=User(name=name,email=email,password=password)
            reg=User(id=2)
            # reg.save()
            reg.delete()
            # reg.update()
            # print('password2:',fm.cleaned_data['password2'])
            # print("agree:",fm.cleaned_data['agree'])
            # print("roll:",fm.cleaned_data['roll'])
            # print("price:",fm.cleaned_data['price'])
            # print("comment",fm.cleaned_data['comment'])
            # print('website:',fm.cleaned_data['website'])
            # print('password:',fm.cleaned_data['password'])
            # print('description:',fm.cleaned_data['description'])
            # print('notes:',fm.cleaned_data['notes'])
            return redirect('success')
    else:
        fm=Registration()
    return render(request,'form/user.html',{'form':fm})
    # return render(request,'form/registration.html',{'form':fm})
    # return render(request,'form/fieldserror.html',{'form':fm})
def success(request):
    return render(request,'form/success.html')

def StRegistarion(request):
    if request.method=='POST':
        fm=ModelRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print('name:',name)
            print('email:',email)
            print("password",password)
            rw=User(name=name,email=email,password=password)
            rw.save()
            fm=ModelRegistration()
            
    # if request.method=='POST':
    #     pi=User.objects.get(pk=1)
    #     fm=StudentRegistration(request.POST,instance=pi)
    #     if fm.is_valid():
    #         fm.save()
    else:
        fm=ModelRegistration()
    return render(request,'form/modelform.html',{"form":fm})


# dynamic url
def showdetails(request,my_id):
    if my_id==1:
        student={'id':my_id,'name':'computer'}
    if my_id==2:
        student={'id':my_id,'name':'Application'}
    if my_id==3:
        student={'id':my_id,'name':'student'}
    return render(request,'form/dynamicurl.html',student)

# show year 
def showyear(request,year):
    student={'year':year}
    return render(request,'form/showyear.html',student)
    