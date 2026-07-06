from apps.core.views import ModeloBaseViewSet
from apps.core.permissions import TienePermisoRol
from ..models.empleado import Empleado
from ..serializers.empleado import (
    EmpleadoListSerializer,
    EmpleadoDetailSerializer,
    EmpleadoCreateSerializer,
    EmpleadoUpdateSerializer,
)

class EmpleadoViewSet(ModeloBaseViewSet):

    queryset = Empleado.objects.all()

    permission_classes = [TienePermisoRol]

    serializer_map = {
        "list": EmpleadoListSerializer,
        "retrieve": EmpleadoDetailSerializer,
        "create": EmpleadoCreateSerializer,
        "update": EmpleadoUpdateSerializer,
        "partial_update": EmpleadoUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action,
            EmpleadoListSerializer
        )