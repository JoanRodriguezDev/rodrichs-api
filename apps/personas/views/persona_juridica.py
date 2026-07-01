from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.persona_juridica import (
    PersonaJuridicaListSerializer,
    PersonaJuridicaDetailSerializer,
    PersonaJuridicaCreateSerializer,
    PersonaJuridicaUpdateSerializer,
)

class PersonaJuridicaViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": PersonaJuridicaListSerializer,
        "retrieve": PersonaJuridicaDetailSerializer,
        "create": PersonaJuridicaCreateSerializer,
        "update": PersonaJuridicaUpdateSerializer,
        "partial_update": PersonaJuridicaUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            PersonaJuridicaListSerializer
        )