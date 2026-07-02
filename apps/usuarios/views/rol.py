from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.rol import (
    RolListSerializer,
    RolDetailSerializer,
    RolCreateSerializer,
    RolUpdateSerializer,
)

class RolViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": RolListSerializer,
        "retrieve": RolDetailSerializer,
        "create": RolCreateSerializer,
        "update": RolUpdateSerializer,
        "partial_update": RolUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            RolListSerializer
        )