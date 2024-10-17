from django.apps import AppConfig
"""
This module defines the configuration for the 'cart' application.
Classes:
    CartConfig: Configures the 'cart' application with default settings.
"""


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
