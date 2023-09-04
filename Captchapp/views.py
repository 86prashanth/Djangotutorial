from django.shortcuts import render
from Captchapp.forms import StudentCaptchaform
from django.contrib import messages 
from Captchapp.send_sms import sendsms

# Create your views here.
def home(request):
    if request.method=='POST':
        form=StudentCaptchaform(request.POST)
        if form.is_valid():
            print("name:",form.cleaned_data['name'])
            print("email:",form.cleaned_data['email'])
            print("captcha:",form.cleaned_data['captcha'])
            form.save()
            messages.success(request,'student-data has been submitted')
            form=StudentCaptchaform()
            sendsms()
    else:
       form=StudentCaptchaform() 
    return render(request,'captcha/captcha.html',{'form':form})