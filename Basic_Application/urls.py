from django.urls import path 
from Basic_Application.views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('home2/',home2,name='home2'),
    path('hyperlinks/',hyperlinks,name='hyperlinks'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]
