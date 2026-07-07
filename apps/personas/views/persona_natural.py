from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.persona_natural import PersonaNatural
from ..serializers.persona_natural import (
    PersonaNaturalListSerializer,
    PersonaNaturalDetailSerializer,
    PersonaNaturalCreateSerializer,
    PersonaNaturalUpdateSerializer,
)

class PersonaNaturalViewSet(ModeloBaseViewSet):

    queryset = PersonaNatural.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": PersonaNaturalListSerializer,
        "retrieve": PersonaNaturalDetailSerializer,
        "create": PersonaNaturalCreateSerializer,
        "update": PersonaNaturalUpdateSerializer,
        "partial_update": PersonaNaturalUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            PersonaNaturalListSerializer
        )