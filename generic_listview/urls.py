from django.urls import path
from generic_listview.views import *

urlpatterns = [
    path('',StudentListView.as_view(),name='home'),
]
