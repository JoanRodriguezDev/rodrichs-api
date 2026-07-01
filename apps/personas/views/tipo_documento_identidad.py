from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..serializers.tipo_documento_identidad import (
    TipoDocumentoIdentidadListSerializer,
    TipoDocumentoIdentidadDetailSerializer,
    TipoDocumentoIdentidadCreateSerializer,
    TipoDocumentoIdentidadUpdateSerializer,
)

class TipoDocumentoIdentidadViewSet(ModeloBaseViewSet):

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": TipoDocumentoIdentidadListSerializer,
        "retrieve": TipoDocumentoIdentidadDetailSerializer,
        "create": TipoDocumentoIdentidadCreateSerializer,
        "update": TipoDocumentoIdentidadUpdateSerializer,
        "partial_update": TipoDocumentoIdentidadUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            TipoDocumentoIdentidadListSerializer
        )