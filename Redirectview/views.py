from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.
class Home(TemplateView):
    template_name ='redirectview/home.html'
    
class Home_RedirectView(RedirectView):
    url='https://www.google.com/'

class Redirect_Home(RedirectView):
    # url='/redirect/'
    pattern_name='redirect'
    permanent=True
    query_string=True
    