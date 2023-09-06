from django.shortcuts import render
from Authentication_app.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm

from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate ,get_user_model
from Authentication_app.forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes,force_str

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from Authentication_app.utils import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
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
    
class MyLoginView:
    pass


class RegisterView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    template_name='auth/register.html'
    
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:
        return HttpResponse('Activation link is invalid!') 
  
    

  
def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('auth/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'auth/signup.html', {'form': form})  