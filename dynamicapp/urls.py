from django.urls import path 
from dynamicapp.views import * 

urlpatterns = [
    path('learn/',learn_django,name='learn_django'),
    path('coursedetails/',course_details,name='course_details'),
    path('models/',models,name='models'),
]
