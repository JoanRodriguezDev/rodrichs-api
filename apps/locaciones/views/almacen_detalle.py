from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.almacen_detalle import AlmacenDetalleStock
from ..serializers.almacen_detalle import (
    AlmacenDetalleListSerializer,
    AlmacenDetalleDetailSerializer,
    AlmacenDetalleCreateSerializer,
    AlmacenDetalleUpdateSerializer,
)

class AlmacenDetalleViewSet(ModeloBaseViewSet):

    queryset = AlmacenDetalleStock.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": AlmacenDetalleListSerializer,
        "retrieve": AlmacenDetalleDetailSerializer,
        "create": AlmacenDetalleCreateSerializer,
        "update": AlmacenDetalleUpdateSerializer,
        "partial_update": AlmacenDetalleUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            AlmacenDetalleListSerializer
        )