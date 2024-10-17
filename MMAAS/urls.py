
"""
URL configuration for the MMAAS project.
This module defines the URL patterns for the MMAAS project, including the admin interface and 
various application-specific routes.
Routes:
    - 'admin/': Admin site URLs.
    - '': Main application URLs.
    - 'products/': Product application URLs.
    - 'cart/': Cart application URLs.
If the DEBUG setting is enabled, it also serves media files during development.
Additionally, it customizes the admin site headers and titles:
    - site_header: 'MMAAS Administration'
    - index_title: 'MMAAS Admin'
    - site_title: 'Administration for MMAAS app'
Imports:
    - admin: Django admin module for site administration.
    - path, include: Django URL handling utilities.
    - static: Utility for serving static files during development.
    - settings: Django settings module for accessing project settings.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls'))
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'MMAAS Administration'                    # default: "Django Administration"
admin.site.index_title = 'MMAAS Admin'                 # default: "Site administration"
admin.site.site_title = 'Admistration for MMAAS app' # default: "Django site admin"


