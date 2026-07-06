from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.permiso import Permiso
from ..serializers.permiso import (
    PermisoListSerializer,
    PermisoDetailSerializer,
    PermisoCreateSerializer,
    PermisoUpdateSerializer,
)

class PermisoViewSet(ModeloBaseViewSet):

    queryset = Permiso.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": PermisoListSerializer,
        "retrieve": PermisoDetailSerializer,
        "create": PermisoCreateSerializer,
        "update": PermisoUpdateSerializer,
        "partial_update": PermisoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            PermisoListSerializer
        )