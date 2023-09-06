from django.urls import path  
from Authentication_app.views import signup, activate  
urlpatterns = [  
    path('signup/', signup, name = 'signup'),  
    path('activate/<uidb64>/<token>/',  
        activate, name='activate'),  
]  