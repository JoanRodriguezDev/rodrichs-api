from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.sucursal import Sucursal
from ..serializers.sucursal import (
    SucursalListSerializer,
    SucursalDetailSerializer,
    SucursalCreateSerializer,
    SucursalUpdateSerializer,
)

class SucursalViewSet(ModeloBaseViewSet):

    queryset = Sucursal.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": SucursalListSerializer,
        "retrieve": SucursalDetailSerializer,
        "create": SucursalCreateSerializer,
        "update": SucursalUpdateSerializer,
        "partial_update": SucursalUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            SucursalListSerializer
        )

