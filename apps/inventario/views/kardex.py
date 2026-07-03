from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.kardex import Kardex
from ..serializers.kardex import (
    KardexListSerializer,
    KardexDetailSerializer,
    KardexCreateSerializer,
    KardexUpdateSerializer,
)

class KardexViewSet(ModeloBaseViewSet):

    queryset = Kardex.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": KardexListSerializer,
        "retrieve": KardexDetailSerializer,
        "create": KardexCreateSerializer,
        "update": KardexUpdateSerializer,
        "partial_update": KardexUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            KardexListSerializer
        )