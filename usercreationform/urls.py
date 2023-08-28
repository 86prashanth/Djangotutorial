from django.urls import path 
from usercreationform.views import * 

urlpatterns = [
    path('',signup,name='signup'),
    path('login/',login_view,name='login'),
    path('profile/',user_profile,name='profile'),
    path('userdetails/<int:id>/',user_details,name='userdetails'),
    path('logout/',user_logout,name='logout'),
    path('changepass/',user_change_pass,name='changepass'),
    path('changepass1/',change_password,name='changepass1'),
    path('dash_board/',dash_board,name='dash_board'),
    path('userdashboard/',user_dashboard,name='user_dashboard'),
]
