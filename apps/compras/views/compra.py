from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.compra import Compra
from ..serializers.compra import (
    CompraListSerializer,
    CompraDetailSerializer,
    CompraCreateSerializer,
    CompraUpdateSerializer,
)

class CompraViewSet(ModeloBaseViewSet):

    queryset = Compra.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": CompraListSerializer,
        "retrieve": CompraDetailSerializer,
        "create": CompraCreateSerializer,
        "update": CompraUpdateSerializer,
        "partial_update": CompraUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            CompraListSerializer
        )