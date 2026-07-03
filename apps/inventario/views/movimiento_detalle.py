from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.movimiento_detalle import MovimientoDetalle
from ..serializers.movimiento_detalle import (
    MovimientoDetalleListSerializer,
    MovimientoDetalleDetailSerializer,
    MovimientoDetalleCreateSerializer,
    MovimientoDetalleUpdateSerializer,
)

class MovimientoDetalleViewSet(ModeloBaseViewSet):

    queryset = MovimientoDetalle.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": MovimientoDetalleListSerializer,
        "retrieve": MovimientoDetalleDetailSerializer,
        "create": MovimientoDetalleCreateSerializer,
        "update": MovimientoDetalleUpdateSerializer,
        "partial_update": MovimientoDetalleUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            MovimientoDetalleListSerializer
        )