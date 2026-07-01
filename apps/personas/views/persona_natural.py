from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.persona_natural import (
    PersonaNaturalListSerializer,
    PersonaNaturalDetailtSerializer,
    PersonaNaturalCreateSerializer,
    PersonaNaturalUpdateSerializer,
)

class PersonaNaturalViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": PersonaNaturalListSerializer,
        "retrieve": PersonaNaturalDetailtSerializer,
        "create": PersonaNaturalCreateSerializer,
        "update": PersonaNaturalUpdateSerializer,
        "partial_update": PersonaNaturalUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            PersonaNaturalListSerializer
        )