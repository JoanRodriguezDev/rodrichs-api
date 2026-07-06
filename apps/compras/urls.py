from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.compra import CompraViewSet

router = DefaultRouter()
router.register(r"compras",CompraViewSet,basename="compras")

urlpatterns = [
    path("",include(router.urls)),
]
