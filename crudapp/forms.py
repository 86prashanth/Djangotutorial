from django.core import validators 
from django import forms 
from .models import Crudapp,User

class CrudRegistration(forms.ModelForm):
    class Meta:
        model=Crudapp
        fields=['id','name','email','password']
    # selecting model forms
        # fields='__all__'
        # exclude=['name']
        # exclude=('name',)
        labels={'name':'Enter your name','email':'Enter your email','password':'Enter your password'}
        error_messages={
            'name':{'required':'Enter Your name'},
            'email':{'required':'Enter Your email'},
            'password':{'required':'Enter Your password'}}
        widgets={'name':forms.TextInput(attrs={'placeholder':'Enter your name','class':'form-control'}),
                 'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control'}),
                 'password':forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'})}
        
        
# model form inheritance
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['student_name','email','password']

class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields=['teacher_name','email','password']