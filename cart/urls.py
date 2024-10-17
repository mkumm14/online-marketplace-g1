from django.urls import path
from . import views

# url patterns for cart app
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('increase_cart_item/<int:cart_item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease_cart_item/<int:cart_item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
        path('remove_discount/', views.remove_discount, name='remove_discount'),
           path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
        path('order_history/', views.order_history, name='order_history'),




]