from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.traslado import Traslado
from ..serializers.traslado import (
    TrasladoListSerializer,
    TrasladoDetailSerializer,
    TrasladoCreateSerializer,
    TrasladoUpdateSerializer,
)

class TrasladoViewSet(ModeloBaseViewSet):

    queryset = Traslado.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": TrasladoListSerializer,
        "retrieve": TrasladoDetailSerializer,
        "create": TrasladoCreateSerializer,
        "update": TrasladoUpdateSerializer,
        "partial_update": TrasladoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            TrasladoListSerializer
        )