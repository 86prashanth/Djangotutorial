from django.urls import path 
from Redirectview.views import * 

urlpatterns = [
    path('<int:pk>/',Home.as_view(),name='home'),
    path('<slug:post>/',Home.as_view(),name='home'),
    path('',Home_RedirectView.as_view(),name='redirect'),
    path('redirect1/',Redirect_Home.as_view(),name='redirect1'),
    
]
