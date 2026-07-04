from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.venta import Venta
from ..serializers.venta import (
    VentaListSerializer,
    VentaDetailSerializer,
    VentaCreateSerializer,
    VentaUpdateSerializer,
)

class VentaViewSet(ModeloBaseViewSet):

    queryset = Venta.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": VentaListSerializer,
        "retrieve": VentaDetailSerializer,
        "create": VentaCreateSerializer,
        "update": VentaUpdateSerializer,
        "partial_update": VentaUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            VentaListSerializer
        )