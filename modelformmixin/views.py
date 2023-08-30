from django.shortcuts import render
from modelformmixin.models import Student
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django import forms
from modelformmixin.forms import StudentForm
# Create your views here.
class StudentCreateView(CreateView):
    model=Student 
    form_class=StudentForm
    # fields=['name','email','password']
    # template_name='mixin/create.html'
    template_name='mixin/create_form.html'
    # success_url='/mixin/thanks/'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        return form
class StudentThankyouTemplate(TemplateView):
    template_name="mixin/thankyou.html"
    
class StudentDetailView(DetailView):
    model=Student
    template_name='mixin/detail.html'
    