from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.proveedor_juridico import (
    ProveedorJuridicoListSerializer,
    ProveedorJuridicoDetailSerializer,
    ProveedorJuridicoCreateSerializer,
    ProveedorJuridicoUpdateSerializer,
)

class ProveedorJuridicoViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ProveedorJuridicoListSerializer,
        "retrieve": ProveedorJuridicoDetailSerializer,
        "create": ProveedorJuridicoCreateSerializer,
        "update": ProveedorJuridicoUpdateSerializer,
        "partial_update": ProveedorJuridicoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ProveedorJuridicoListSerializer
        )