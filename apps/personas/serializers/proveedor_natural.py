from rest_framework import serializers
from ..models.proveedor_natural import ProveedorNatural
from ..models.proveedor import Proveedor
from ..models.persona_natural import PersonaNatural
from ..serializers.proveedor import ProveedorListSerializer
from ..serializers.persona_natural import PersonaNaturalListSerializer

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

# POST /api/v1/proveedores-naturales/ 
# crear un nuevo dato
class ProveedorNaturalCreateSerializer(serializers.ModelSerializer):
    proveedor = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all()
    )

    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = ProveedorNatural
        fields = [
            "proveedor",
            "persona_natural",
        ]

# PUT / PATCH /api/v1/proveedores-naturales/{id} 
# actualizar completo o parcialmente un elemento
class ProveedorNaturalUpdateSerializer(serializers.ModelSerializer):
    proveedor = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all()
    )

    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = ProveedorNatural
        fields = [
            "proveedor",
            "persona_natural",
        ]
