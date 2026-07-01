from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.cliente import (
    ClienteListSerializer,
    ClienteDetailSerializer,
    ClienteCreateSerializer,
    ClienteUpdateSerializer,
)

class ClienteViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ClienteListSerializer,
        "retrieve": ClienteDetailSerializer,
        "create": ClienteCreateSerializer,
        "update": ClienteUpdateSerializer,
        "partial_update": ClienteUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ClienteListSerializer
        )