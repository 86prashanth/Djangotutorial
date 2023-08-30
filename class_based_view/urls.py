from django.urls import path 
from class_based_view.views import *


urlpatterns = [
    path('fun/',myview,name='home'),
    path('cl/',MyView.as_view(name='rajinikanth'),name='cl'),
    path('subcl/',MyViewChild.as_view(),name='subcl'),
    path('homecl/',HomeClassView.as_view(),name='homecls'),
    path('about/',aboutfun,name='about'),
    path('aboutcbv/',AboutClassView.as_view(),name='aboutcv'),
    path('contactfun/',contactfun,name='contactfun'),
    path('contactcv/',ContactClassView.as_view(),name='contactcv'),
    # path('newsfun/',newsfun,name='newsfun'),
    path('newsfun/',newsfun,{'template_name':'cbv/news.html'},name='newsfun'),
    # path('newscv/',NewsClassView.as_view(),name='newscl'),
    path('newscv/',NewsClassView.as_view(template_name='cbv/news.html'),name='newscl'),
]
