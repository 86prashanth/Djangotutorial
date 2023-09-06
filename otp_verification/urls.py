from django.contrib import admin
from django.urls import path
from otp_verification.views import *

urlpatterns = [
    path('',main,name='main'),
    path('auth/',auth_view,name='auth'),
    path('verify/',verify_view,name='verify'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name ='user_login'),
    path('verify-otp/', OTPVerificationView.as_view(), name='otp_verification'),
]
