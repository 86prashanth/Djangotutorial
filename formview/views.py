from django.shortcuts import render
from django.http import HttpResponse
from formview.forms import ContactForm,FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# Create your views here.
class ContactFormView(FormView):
    template_name='formview/contact.html'
    # form_class=ContactForm
    form_class=FeedbackForm
    success_url='/formview/thankyou/'
    # def form_valid(self,form):
    #     print(form)
    #     print(form.cleaned_data['name'])
    #     print(form.cleaned_data['email'])
    #     print(form.cleaned_data['msg'])
    #     # return super().form_valid(form)
    #     return HttpResponse('msg sent')
class Thankyou(TemplateView):
    template_name='formview/thankyou.html'
    
