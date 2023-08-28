from django.shortcuts import render,redirect
from usercreationform.forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,UserCreationForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
# Create your views here.
# signup
def signup(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Editor')
            user.groups.add(group)
            messages.success(request,'ACCOUNT CREATED success')
            fm=SignUpForm()
    else:
        fm=SignUpForm()
    return render(request,'usercreation/signup.html',{'form':fm})

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
                fm=AuthenticationForm()
        return render(request,'usercreation/login.html',{'form':fm})
    else:
        return redirect('profile')

def dash_board(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('dash_board')
        else:
                fm=AuthenticationForm()
        return render(request,'usercreation/dashboard.html',{'form':fm})
    else:
        return redirect('dash_board')
    
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'usercreation/dashboard.html',{'name':request.user.username})
    else:
        return redirect('login')

 
# def profile(request):
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser==True:
                fm=EditAdminprofile(request.POST,instance=request.user)
                users=User.objects.all()    
            else:
                fm=EditUserprofile(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                messages.success(request,'profile updated')
                fm.save()
        else:
            if request.user.is_superuser==True:
                fm=EditAdminprofile(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserprofile(instance=request.user)
                users=None
        return render(request,'usercreation/profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed successfully')
                return redirect('profile')
        else:
            fm=PasswordChangeForm()
        return render(request,'usercreation/changepass.html',{'form':fm})
    else:
        return redirect('profile')
def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed successfully')
                return redirect('profile')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'usercreation/setpswd.html',{'form':fm})
    else:
        return redirect('profile')
    
    
def user_details(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminprofile(instance=pi)
        return render(request,'usercreation/detail.html',{'name':request.user,'form':fm})
    else:
        return redirect('login')