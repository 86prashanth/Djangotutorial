from django.urls import path
from payment_Gateway.views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home-page'),
    path('profile/', UserProfile.as_view(), name='user-profile' ),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('product-list/', product_list, name='product-list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('cart/', view_cart, name='cart'),
    path('increase-cart-item/<int:product_id>/', increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/', decrease_cart_item, name='decrease-cart-item'),
    path('fetch-cart-count/', fetch_cart_count, name='fetch-cart-count'),
    path('create-order/', create_order, name='create-order'),
    path('handle-payment/', handle_payment, name='handle-payment'),
    path('checkout/', checkout, name='checkout'),
]
