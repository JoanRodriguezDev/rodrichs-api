from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.caja_detalle import CajaDetalle
from ..serializers.caja_detalle import (
    CajaDetalleListSerializer,
    CajaDetalleDetailSerializer,
    CajaDetalleCreateSerializer,
    CajaDetalleUpdateSerializer,
)

class CajaDetalleViewSet(ModeloBaseViewSet):

    queryset = CajaDetalle.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": CajaDetalleListSerializer,
        "retrieve": CajaDetalleDetailSerializer,
        "create": CajaDetalleCreateSerializer,
        "update": CajaDetalleUpdateSerializer,
        "partial_update": CajaDetalleUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            CajaDetalleListSerializer
        )