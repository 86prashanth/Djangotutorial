from django.urls import path 
from model_relationship.views import *

urlpatterns = [
    path('',one_to_one,name='home')
]
