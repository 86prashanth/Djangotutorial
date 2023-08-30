from django.urls import path 
from genericdetailview.views import *


urlpatterns = [
    path('student/<int:id>/',StudentDetailView.as_view(),name='detail'),
    path('list/',StudentListView.as_view(),name='studentlist'),
]
