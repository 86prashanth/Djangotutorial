from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
@login_required
def profile(request):
    return render(request,'registration/profile.html',{'name':request.user})


# class ProfileTemplateView(TemplateView):
#     template_name='registration/profileview.html'
@method_decorator(login_required,name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name='registration/profileview.html'
    success_url='/accounts/dashboard/'
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

@staff_member_required
def about(request):
    return render(request,'registration/about.html')

# class AboutTemplateView(TemplateView):
#     template_name='registration/aboutview.html'
@method_decorator(staff_member_required,name='dispatch')
class AboutTemplateView(TemplateView):
    template_name='registration/aboutview.html'
    
    
class Dashboard(TemplateView):
    template_name='customauth/dashboard.html'
    
    
class LogoutView(TemplateView):
    template_name='customauth/logout.html'
    
class LoginView(TemplateView):
    template_name=''
    success_url='accounts/dashboard'
    
class LogoutView(TemplateView):
    template_name=''

class PasswordChangeView(TemplateView):
    authentication_form=PasswordChangeForm
    template_name=''
    
class PasswordChangeDoneView(TemplateView):
    template_name=''
    