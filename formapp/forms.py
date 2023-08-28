from django import forms 
from django.core import validators 
from formapp.models import User 

class StudentRegistration(forms.Form):
    name=forms.CharField()
    # name=forms.CharField(label='Your Name',label_suffix='',initial='your name...',required=False,disabled=True, help_text="limit 70 characaters")
    password=forms.CharField(widget=forms.PasswordInput())
    # upload=forms.CharField(widget=forms.FileInput())
    # checkbox=forms.CharField(widget=forms.CheckboxInput)
    # email=forms.EmailField()
    # first_name=forms.CharField()
    # mobile=forms.IntegerField()
    # key=forms.CharField(widget=forms.HiddenInput())
    
    #  start with  characaters 
    
def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError("name should be start with s")

class Registration(forms.Form):
    # name=forms.CharField()
    # name=forms.CharField(empty_value='sds')
    # name=forms.CharField(validators=[start_with_s])
    # password=forms.CharField(widget=forms.PasswordInput)
    # password2=forms.CharField(widget=forms.PasswordInput,label='Password(again)')
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valpwd=self.cleaned_data['password']
    #     valpwd2=self.cleaned_data['password2']
    #     if valpwd != valpwd2:
    #         raise forms.ValidationError('password does not match')
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valpwd=self.cleaned_data['password']
    #     valrpwd=self.cleaned_data['password2']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('password does not match')
    # name=forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name=forms.CharField(error_messages={'required':'Enter your name'})
    # name=forms.CharField(min_length=5,max_length=50,strip=False)
    email=forms.EmailField(error_messages={'required':'Enter your email'})
    password=forms.CharField(error_messages={'required':'Enter your password'},widget=forms.PasswordInput)
    # roll=forms.IntegerField(min_value=5,max_value=50)
    # price=forms.DecimalField(max_digits=40,decimal_places=1)
    # rate=forms.FloatField(min_value=5,max_value=40)
    # comment=forms.SlugField()
    # email=forms.EmailField(min_length=5,max_length=50)
    # website=forms.URLField(min_length=5,max_length=50)
    # password=forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
    # description=forms.CharField(widget=forms.Textarea)
    # feedback=forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))
    # notes=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':4}))
    # agree=forms.BooleanField(label='I agree',label_suffix='')
    
    
    # validators 
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<4:
    #         raise forms.ValidationError('enter more than or equal 4 char')
    #     return valname
    
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if len(valemail)<10:
    #         raise forms.ValidationError('Email should be more than or equal 10')
    #     return valemail
    
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<4:
    #         raise forms.ValidationError('name should be more than or equal 4')
    #     if len(valemail)<10:
    #         raise forms.ValidationError('Email should be more than or equl 10')
            
        
# model forms 
class ModelRegistration(forms.ModelForm):
    class Meta:
        model=User 
        fields=['name','email','password']
        error_messages={
            'password':{'required':'Enter your password'},
            'name':{'required':'Enter your name'},
            'email':{'required':'Enter your email'}
        }
        labels={'name':'Enter your name','password':'Enter your password','email':'Enter your Email'}
        help_text={'name':'Enter your full name'}
       
        widgets={'password':forms.PasswordInput,'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter your name'})}