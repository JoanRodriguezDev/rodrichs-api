from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.producto import (
    ProductoListSerializer,
    ProductoDetailSerializer,
    ProductoCreateSerializer,
    ProductoUpdateSerializer,
)

class ProductoViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": ProductoListSerializer,
        "retrieve": ProductoDetailSerializer,
        "create": ProductoCreateSerializer,
        "update": ProductoUpdateSerializer,
        "partial_update": ProductoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            ProductoListSerializer
        )