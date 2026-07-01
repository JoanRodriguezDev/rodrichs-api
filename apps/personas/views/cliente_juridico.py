from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.cliente_juridico import (
    ClienteJuridicoListSerializer,
    ClienteJuridicoDetailSerializer,
    ClienteJuridicoCreateSerializer,
    ClienteJuridicoUpdateSerializer,
)

class ClienteJuridicoViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ClienteJuridicoListSerializer,
        "retrieve": ClienteJuridicoDetailSerializer,
        "create": ClienteJuridicoCreateSerializer,
        "update": ClienteJuridicoUpdateSerializer,
        "partial_update": ClienteJuridicoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ClienteJuridicoListSerializer
        )