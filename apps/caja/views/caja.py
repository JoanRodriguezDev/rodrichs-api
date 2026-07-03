from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.caja import (
    CajaListSerializer,
    CajaDetailSerializer,
    CajaCreateSerializer,
    CajaUpdateSerializer,
)

class CajaViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": CajaListSerializer,
        "retrieve": CajaDetailSerializer,
        "create": CajaCreateSerializer,
        "update": CajaUpdateSerializer,
        "partial_update": CajaUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            CajaListSerializer
        )