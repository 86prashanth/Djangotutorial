from django.urls import path 
from pagecounter.views import *
from django.views.decorators.cache import cache_page
from pagecounter.signals import *

urlpatterns = [
    path('',home,name='home'),
    path('cache_page/',cache_page,name='cache_page'),
    path('contact/',contact_page,name='contact_page'),
    path('ipaddress/',ip_address,name='ipaddress'),
    path('logincount/',login_count,name='logincount'),
    path('notification/',custom_signals,name='notification'),
]
