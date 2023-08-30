from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name='template_view/home.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']='prashant'
        context['roll']=101
        # context={'name':'prashanth','roll':'101'}
        print(context)
        print(kwargs)
        return context