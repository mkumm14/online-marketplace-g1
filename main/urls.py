from django.urls import path
"""
URL configuration for the main app.
This module defines the URL patterns for the main app, mapping URLs to their corresponding view functions.
Routes:
- '' : Maps to the index view.
- 'home/' : Maps to the home view.
- 'login/' : Maps to the login_view.
- 'logout/' : Maps to the logout_view.
- 'register/' : Maps to the register_view.
- 'about/' : Maps to the about view.
Variables:
- app_name (str): The namespace for the main app URLs.
- urlpatterns (list): A list of URL patterns for the main app.
"""
from . import views


app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view,name="logout"),
    path('register/', views.register_view,name='register'),
    path('about/', views.about, name='about'),
]
