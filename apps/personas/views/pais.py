from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.pais import Pais
from ..serializers.pais import (
    PaisListSerializer,
    PaisCreateSerializer,
    PaisDetailSerializer,
    PaisUpdateSerializer,
)

class PaisViewSet(ModeloBaseViewSet):

    queryset = Pais.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": PaisListSerializer,
        "retrieve": PaisDetailSerializer,
        "create": PaisCreateSerializer,
        "update": PaisUpdateSerializer,
        "partial_update": PaisUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            PaisListSerializer
        )