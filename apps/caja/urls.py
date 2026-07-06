from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.caja import CajaViewSet
from .views.caja_detalle import CajaDetalleViewSet

router = DefaultRouter()
router.register(r"cajas",CajaViewSet,basename="cajas")
router.register(r"caja-detalles",CajaDetalleViewSet,basename="caja-detalles")

urlpatterns = [
    path("",include(router.urls)),
]
