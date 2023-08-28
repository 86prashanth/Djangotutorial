from django.urls import path 
from templates_app.views import * 

urlpatterns = [
    path('courseone/',learndj,name='learndj'),
    path('coursetwo/',coursetwo,name='coursetwo'),
    path('feesone/',feesone,name='feesone'),
    path('feestwo/',feestwo,name='feestwo'),
]
