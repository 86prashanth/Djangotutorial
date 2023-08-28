from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms 

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confrim password(again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        labeles={'email':'Email',}
        
class EditUserprofile(UserChangeForm):
    password=None 
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','date_joined','last_login','is_active']
        labels={'email':'Email'}
class EditAdminprofile(UserChangeForm):
    password=None 
    class Meta:
        model=User
        fields='__all__'
        # fields=['username','email','first_name','last_name','date_joined','last_login','is_active']
        labels={'email':'Email'}