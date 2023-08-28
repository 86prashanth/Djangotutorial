from django.urls import path 
from crudapp.views import * 

urlpatterns = [
    path('',addshow,name='addshow'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete_data,name='delete'),
    path('teacher_form/',teacher_form,name='teacher_form'),
    path('user_form/',user_form,name='user_form'),
]
