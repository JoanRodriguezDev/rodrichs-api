from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.persona_juridica import PersonaJuridica
from ..serializers.persona_juridica import (
    PersonaJuridicaListSerializer,
    PersonaJuridicaDetailSerializer,
    PersonaJuridicaCreateSerializer,
    PersonaJuridicaUpdateSerializer,
)

class PersonaJuridicaViewSet(ModeloBaseViewSet):

    queryset = PersonaJuridica.objects.all()

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