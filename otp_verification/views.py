from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
# from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

from otp_verification.utils import send_sms_otp
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required




class OTPVerificationView(View):
    def post(self, request):
        submitted_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        password = request.session.get('password')
        
        if submitted_otp == saved_otp:
            messages.success(request, "OTP verification successful")
            phone_number = request.session.get('phone_number')
            User = get_user_model()
            user = User.objects.create(phone_number=phone_number)
            user.set_password(password)
            user.save()
            return redirect('user_login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('otp_verification')
        
class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'otpverification/registration.html', {'form': form, 'otp_required': False})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
    
        if form.is_valid():
            phone_number = str(form.cleaned_data['phone_number'])
            verification_method = form.cleaned_data['verification_method']
            try:
                if 'otp' in request.POST:
                    return OTPVerificationView.as_view()(request)
                else:
                    password = form.cleaned_data['password']
                    otp = generate_otp()
                    print(otp)
                    if verification_method == 'sms':
                        send_sms_otp(phone_number, otp)
                      
            except:   
                request.session['otp'] = otp
                request.session['phone_number'] = phone_number
                request.session['password'] = password
                form.fields['password'].widget.attrs['value'] = password

                return render(request, 'otpverification/registration.html', {'form': form, 'otp_required': True, 'password': password})

        return render(request, 'otpverification/registration.html', {'form': form, 'otp_required': False})

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'otpverification/login.html', {'form': form})
    
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            messages.success(request,'Login SuccessFul')
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            otp = form.cleaned_data['otp']
            
        
        return render(request, 'otpverification/login.html',{'form':form})
    
def generate_otp():
    return str(random.randint(100000, 999999))




# Create your views here.
@login_required
def main(request):
    return render(request,'main.html')


def auth_view(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('verify')
    return render(request,'verify/auth.html',{"form":form})


def verify_view(request):
    form=CodeForm(request.POST or None)
    pk=request.session.get('pk')
    if pk:
        user=CustomUser.objects.get(pk=pk)
        code=user.code 
        code_user=f"{user.username} : {user.code}"
        if not request.POST:
            print(code_user)
            sendsms(code_user,user.phone_number)
        if form.is_valid():
            num=form.cleaned_data.get('number')
            if str(code)==num:
                code.save()
                login(request,user)
                return redirect('home')
            else:
                return redirect('auth')
    return render(request,'verify/verify.html',{"form":form})



