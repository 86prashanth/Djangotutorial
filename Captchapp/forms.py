from django import forms 
from Captchapp.models import Student_captcha
from captcha.fields import CaptchaField

class StudentCaptchaform(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Student_captcha
        fields=['name','email','captcha']
        widgets={'name':forms.TextInput,'email':forms.EmailInput}
