from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.cliente_natural import (
    ClienteNaturalListSerializer,
    ClienteNaturalDetailSerializer,
    ClienteNaturalCreateSerializer,
    ClienteNaturalUpdateSerializer,
)

class ClienteNaturalViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ClienteNaturalListSerializer,
        "retrieve": ClienteNaturalDetailSerializer,
        "create": ClienteNaturalCreateSerializer,
        "update": ClienteNaturalUpdateSerializer,
        "partial_update": ClienteNaturalUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ClienteNaturalListSerializer
        )