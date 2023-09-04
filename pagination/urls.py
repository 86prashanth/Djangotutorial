from django.urls import path
from pagination.views import * 

urlpatterns = [
    path('page/',post,name='page'),
    path('pagecbv/',PostListView.as_view(),name='pagecbv'),
    path('pagedetail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    
]
