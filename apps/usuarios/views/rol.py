from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.rol import Rol
from ..serializers.rol import (
    RolListSerializer,
    RolDetailSerializer,
    RolCreateSerializer,
    RolUpdateSerializer,
)

class RolViewSet(ModeloBaseViewSet):

    queryset = Rol.objects.all()

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