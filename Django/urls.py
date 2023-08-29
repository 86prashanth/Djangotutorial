"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from multiapplication.views import *
from core.views import *
from dynamicapp.urls import *
from formapp.urls import *
from crudapp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Basic_Application.urls')),
    path('cor/',include([
        path('learndj/',learndj,name='learndj'),
        path('learnpython/',learnpython,name='learnpython'),
        path('static/',staticapp,name='staticapp'),
        path('set/',setcookie,name='setcookie'),
        path('get/',getcookie,name='getcookie'),
        path('delete/',deletecookie,name='deletecookie'),
        path('setsession/',setsession,name='setsession'),
        path('getsession/',getsession,name='getsession'),
        path('delsession/',deletesession,name='delsession'),
        path('midware/',mid_ware,name='midware'),
        path('mymidware/',mymidware,name='mymidware'),
        path('myprocess/',myprocess,name='myprocess'),
        path('exception/',myexception,name='myexception'),
        path('user/',user_info,name='user'),
        path('under/',undercon,name='undercon'),


    ])),
    path('mul/',include([
        path('feedj/',fee_django,name='fee_django'),
        path('feepy/',fee_python,name='fee_py'),
    ])),
    path('templates/',include('templates_app.urls')),
    path('dynamic/',include('dynamicapp.urls')),
    path('form/',include('formapp.urls')),
    path('crud/',include('crudapp.urls')),
    path('message/',include('messageframe.urls')),
    path('usercreationform/',include('usercreationform.urls')),
    path('pagecount/',include('pagecounter.urls')),
    path('queryset/',include('querysetapi.urls')),
    path('model_inher/',include('model_inheritance.urls')),
    path('manager/',include('manager_app.urls')),
    path('msrelation/',include('model_relationship.urls')),
        
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)