from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.cliente_natural import ClienteNatural
from ..serializers.cliente_natural import (
    ClienteNaturalListSerializer,
    ClienteNaturalDetailSerializer,
    ClienteNaturalCreateSerializer,
    ClienteNaturalUpdateSerializer,
)

class ClienteNaturalViewSet(ModeloBaseViewSet):

    queryset = ClienteNatural.objects.all()

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