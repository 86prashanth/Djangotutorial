from django.urls import path 
from Otp_Verfication.views import  * 

urlpatterns = [
    path('',send_otp,name='send_otp')
]
