from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.proveedor_natural import (
    ProveedorNaturalListSerializer,
    ProveedorNaturalDetailSerializer,
    ProveedorNaturalCreateSerializer,
    ProveedorNaturalUpdateSerializer,
)

class ProveedorNaturalViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ProveedorNaturalListSerializer,
        "retrieve": ProveedorNaturalDetailSerializer,
        "create": ProveedorNaturalCreateSerializer,
        "update": ProveedorNaturalUpdateSerializer,
        "partial_update": ProveedorNaturalUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ProveedorNaturalListSerializer
        )