from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.sucursal import SucursalViewSet
from .views.almacen import AlmacenViewSet
from .views.almacen_detalle import AlmacenDetalleViewSet

router = DefaultRouter()
router.register(r"sucursales",SucursalViewSet,basename="sucursales")
router.register(r"almacenes",AlmacenViewSet,basename="sucualmacenesrsales")
router.register(r"almacen-detalles",AlmacenDetalleViewSet,basename="almacen-detalles")

urlpatterns = [
    path("",include(router.urls)),
]
