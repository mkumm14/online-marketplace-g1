from django.apps import AppConfig
"""
This module defines the configuration for the 'product' application.
Classes:
    ProductConfig(AppConfig): Configuration class for the 'product' application.
"""


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
