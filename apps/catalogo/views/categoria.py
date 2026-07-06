from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.categoria import Categoria
from ..serializers.categoria import (
    CategoriaListSerializer,
    CategoriaDetailSerializer,
    CategoriaCreateSerializer,
    CategoriaUpdateSerializer,
)

class CategoriaViewSet(ModeloBaseViewSet):

    queryset = Categoria.objects.all()

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