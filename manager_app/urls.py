from django.urls import path 
from manager_app.views import * 


urlpatterns = [
    path('',manager_home,name='manger'),
]
