from django.urls import path 
from TemplateView.views import * 


urlpatterns = [
    path('home/',HomeView.as_view(template_name='template_view/home.html',extra_context={'course':'python'}),name='home'),
    path('home/<int:cl>/',HomeView.as_view(template_name='template_view/home.html',extra_context={'course':'python'}),name='cl'),
]
