from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('increase_cart_item/<int:cart_item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease_cart_item/<int:cart_item_id>/', views.decrease_cart_item, name='decrease_cart_item'),

]