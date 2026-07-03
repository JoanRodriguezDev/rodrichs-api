from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.almacen import Almacen
from ..serializers.almacen import (
    AlmacenListSerializer,
    AlmacenDetailSerializer,
    AlmacenCreateSerializer,
    AlmacenUpdateSerializer,
)

class AlmacenViewSet(ModeloBaseViewSet):

    queryset = Almacen.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": AlmacenListSerializer,
        "retrieve": AlmacenDetailSerializer,
        "create": AlmacenCreateSerializer,
        "update": AlmacenUpdateSerializer,
        "partial_update": AlmacenUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            AlmacenListSerializer
        )