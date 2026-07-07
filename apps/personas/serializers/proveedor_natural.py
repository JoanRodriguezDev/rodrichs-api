from rest_framework import serializers
from ..models.proveedor_natural import ProveedorNatural
from ..models.proveedor import Proveedor
from ..models.persona_natural import PersonaNatural
from ..serializers.proveedor import ProveedorListSerializer
from ..serializers.persona_natural import PersonaNaturalListSerializer
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/proveedores-naturales/ 
# consultar todo los datos
class ProveedorNaturalListSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)

    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = ProveedorNatural
        fields = [
            "id",
            "proveedor",
            "persona_natural",
        ]

# GET /api/v1/proveedores-naturales/{id}/ 
# consultar un dato en específico
class ProveedorNaturalDetailSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)
    
    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = ProveedorNatural
        fields = [
            "id",
            "proveedor",
            "persona_natural",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class ProveedorNaturalBaseSerializer(ModeloBaseSerializer):

    proveedor = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all()
    )

    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = ProveedorNatural
        fields = (
            "proveedor",
            "persona_natural",
        )

    def validate_proveedor(self, value):

        if value.tipo != Proveedor.Tipo.NATURAL:
            raise serializers.ValidationError(
                "El proveedor debe ser de tipo natural."
            )

        return value
    
# POST /api/v1/proveedores-naturales/ 
# crear un nuevo dato
class ProveedorNaturalCreateSerializer(ProveedorNaturalBaseSerializer):
    pass

# PUT / PATCH /api/v1/proveedores-naturales/{id} 
# actualizar completo o parcialmente un elemento
class ProveedorNaturalUpdateSerializer(ProveedorNaturalBaseSerializer):
    pass
