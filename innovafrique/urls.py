"""
URL configuration for innovafrique project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from payments.views import admin_dashboard

# Personnalisation de l'admin
admin.site.site_header = "InnovAfrique Administration"
admin.site.site_title = "InnovAfrique Admin"
admin.site.index_title = "Bienvenue sur InnovAfrique"

urlpatterns = [
    path("admin/dashboard/", admin_dashboard, name='admin_dashboard'),
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("accounts/", include("accounts.urls")),
    path("payments/", include("payments.urls")),
]

# Servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
