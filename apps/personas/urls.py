from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.tipo_documento_identidad import TipoDocumentoIdentidadViewSet
from .views.pais import PaisViewSet
from .views.persona_natural import PersonaNaturalViewSet
from .views.persona_juridica import PersonaJuridicaViewSet
from .views.cliente import ClienteViewSet
from .views.proveedor import ProveedorViewSet
from .views.cliente_natural import ClienteNaturalViewSet
from .views.cliente_juridico import ClienteJuridicoViewSet
from .views.proveedor_natural import ProveedorNaturalViewSet
from .views.proveedor_juridico import ProveedorJuridicoViewSet

router = DefaultRouter()
router.register(r'tipo-documento',TipoDocumentoIdentidadViewSet,basename='tipo-documento')
router.register(r'paises',PaisViewSet,basename='paises')
router.register(r'personas',PersonaNaturalViewSet,basename='personas')
router.register(r'empresas',PersonaJuridicaViewSet,basename='empresas')
router.register(r'clientes',ClienteViewSet,basename='clientes')
router.register(r'proveedores',ProveedorViewSet,basename='proveedores')
router.register(r'clientes-naturales',ClienteNaturalViewSet,basename='clientes-naturales')
router.register(r'clientes-empresas',ClienteJuridicoViewSet,basename='clientes-empresas')
router.register(r'proveedores-naturales',ProveedorNaturalViewSet,basename='proveedores-naturales')
router.register(r'proveedores-empresas',ProveedorJuridicoViewSet,basename='proveedores-empresas')

urlpatterns = [
    path('',include(router.urls)),
]