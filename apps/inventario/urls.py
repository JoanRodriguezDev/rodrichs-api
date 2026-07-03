from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.movimiento import MovimientoViewSet
from .views.movimiento_detalle import MovimientoDetalleViewSet
from .views.kardex import KardexViewSet

router = DefaultRouter()
router.register(r'movimientos',MovimientoViewSet,basename='movimientos')
router.register(r'movimiento-detalles',MovimientoDetalleViewSet,basename='movimiento-detalles')
router.register(r'kardex',KardexViewSet,basename='kardex')

urlpatterns = [
    path('',include(router.urls)),
]
