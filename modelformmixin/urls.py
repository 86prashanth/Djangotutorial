from django.urls import path 
from modelformmixin.views import * 
from modelformmixin.updateview import *
from modelformmixin.deleteview import *

urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='create'),
    path('thanks/',StudentThankyouTemplate.as_view(),name='thanks'),
    path('detail/<int:pk>/',StudentDetailView.as_view(),name='detail'),
    path('updatecreate/',StudentUpdateCreateView.as_view(),name='updatecreate'),
    path('updateview/<int:pk>/',StudentUpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',StudentDeleteview.as_view(),name='deleteview'),
    path('thanksupdate/',ThanksUpdateview.as_view(),name='thanksupdate'),
]
