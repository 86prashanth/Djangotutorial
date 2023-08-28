from django.urls import path ,register_converter
from . import views,converters 
# from .converters import *

register_converter(converters.FourDigityearConverter,'yyyy')
urlpatterns = [
    path('',views.showfromdata,name='showfromdata'),
    path("registration/",views.ShowRegistration,name='register'),
    path('success/',views.success,name='success'),
    path('modelform/',views.StRegistarion,name='modelform'),
    # path('showdetails/<my_id>',showdetails,name='showdetail'),
    path('showdetails/<int:my_id>',views.showdetails,name='detail'),
    path("session/<yyyy:year>/",views.showyear,name='year')
]
