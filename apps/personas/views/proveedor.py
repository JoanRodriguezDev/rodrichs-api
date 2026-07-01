from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.proveedor import (
    ProveedorListSerializer,
    ProveedorDetailSerializer,
    ProveedorCreateSerializer,
    ProveedorUpdateSerializer,
)

class ProveedorViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ProveedorListSerializer,
        "retrieve": ProveedorDetailSerializer,
        "create": ProveedorCreateSerializer,
        "update": ProveedorUpdateSerializer,
        "partial_update": ProveedorUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ProveedorListSerializer
        )