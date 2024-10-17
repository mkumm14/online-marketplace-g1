from django.apps import AppConfig
"""
This module defines the configuration for the 'main' application in a Django project.
Classes:
    MainConfig(AppConfig): Configuration class for the 'main' application.
        Attributes:
            default_auto_field (str): Specifies the type of auto field to use for primary keys.
            name (str): The name of the application.
"""


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
