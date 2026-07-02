from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.usuario import (
    UsuarioListSerializer,
    UsuarioDetailSerializer,
    UsuarioCreateSerializer,
    UsuarioUpdateSerializer,
)

class UsuarioViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": UsuarioListSerializer,
        "retrieve": UsuarioDetailSerializer,
        "create": UsuarioCreateSerializer,
        "update": UsuarioUpdateSerializer,
        "partial_update": UsuarioUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            UsuarioListSerializer
        )