from django.urls import path
from . import views


app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view,name="logout"),
    path('register/', views.register_view,name='register'),
    path('checkout/', views.checkout, name="Checkout"),
    path('cart/', views.cart, name="cart"),
    path('store/', views.store, name="store"),
    path('about/', views.about, name='about'),
]
