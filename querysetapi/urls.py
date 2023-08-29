from django.urls import path
from querysetapi.views import *


urlpatterns = [
    path('',home,name='home'),
    # path('queryset/<int:pk>',queryset,name='queryset'),
    path('queryset/',queryset,name='queryset'),
    path('fieldlookup/',fieldlookup,name='fieldlookup'),
    path('agree/',agree,name='agree'),
    path('qobject/',Qobject,name='qobject'),
]
