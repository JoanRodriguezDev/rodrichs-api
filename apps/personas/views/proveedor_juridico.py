from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.proveedor_juridico import ProveedorJuridico
from ..serializers.proveedor_juridico import (
    ProveedorJuridicoListSerializer,
    ProveedorJuridicoDetailSerializer,
    ProveedorJuridicoCreateSerializer,
    ProveedorJuridicoUpdateSerializer,
)

class ProveedorJuridicoViewSet(ModeloBaseViewSet):

    queryset = ProveedorJuridico.objects.all()

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