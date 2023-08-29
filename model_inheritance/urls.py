from django.urls import path
from model_inheritance.views import * 


urlpatterns = [
    path('',home,name='home'),
]
