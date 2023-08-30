from django.urls import * 
from .views import * 

urlpatterns = [
    path('',ContactFormView.as_view(),name='contact'),
    path('thankyou/',Thankyou.as_view(),name='thankyou')
]
