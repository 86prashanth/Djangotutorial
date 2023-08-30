from django.urls import path
from pagination.views import * 

urlpatterns = [
    path('',post,name='home'),
    
]
