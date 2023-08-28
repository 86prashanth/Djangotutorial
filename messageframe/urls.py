from django.urls import path 
from messageframe.views import reg

urlpatterns = [
    path('',reg,name='reg')
]
