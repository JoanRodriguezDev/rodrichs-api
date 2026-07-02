from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.categoria import (
    CategoriaListSerializer,
    CategoriaDetailSerializer,
    CategoriaCreateSerializer,
    CategoriaUpdateSerializer,
)

class CategoriaViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": CategoriaListSerializer,
        "retrieve": CategoriaDetailSerializer,
        "create": CategoriaCreateSerializer,
        "update": CategoriaUpdateSerializer,
        "partial_update": CategoriaUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            CategoriaListSerializer
        )