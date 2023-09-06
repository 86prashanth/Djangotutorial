from django.urls import path 
from verifcation_otp.views import * 

urlpatterns = [
    path('',home_view,name='home_view'),
    path('auth/',auth_view,name='auth'),
    path('verify/',verify_view,name='verify'),
]
