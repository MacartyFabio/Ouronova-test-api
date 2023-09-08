from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dividends.api import viewsets, openapi
from django.conf.urls.static import static
from django.conf import settings
from ninja import NinjaAPI


rota = routers.DefaultRouter()
rota.register(r"dividends", viewsets.DividendsViewSet, basename="Dividends")

api = NinjaAPI()
api.add_router("", openapi.router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(rota.urls)),
    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
