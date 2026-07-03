from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.movimiento import Movimiento
from ..serializers.movimiento import (
    MovimientoListSerializer,
    MovimientoDetailSerializer,
    MovimientoCreateSerializer,
    MovimientoUpdateSerializer,
)

class MovimientoViewSet(ModeloBaseViewSet):

    queryset = Movimiento.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": MovimientoListSerializer,
        "retrieve": MovimientoDetailSerializer,
        "create": MovimientoCreateSerializer,
        "update": MovimientoUpdateSerializer,
        "partial_update": MovimientoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            MovimientoListSerializer
        )
