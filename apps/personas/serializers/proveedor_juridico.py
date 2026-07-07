from rest_framework import serializers
from ..models.proveedor_juridico import ProveedorJuridico
from ..models.proveedor import Proveedor
from ..models.persona_juridica import PersonaJuridica
from ..serializers.proveedor import ProveedorListSerializer
from ..serializers.persona_juridica import PersonaJuridicaListSerializer
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/proveedores-empresas/ 
# consultar todo los datos
class ProveedorJuridicoListSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)

    persona_juridica = PersonaJuridicaListSerializer(read_only=True)

    class Meta:
        model = ProveedorJuridico
        fields = [
            "id",
            "proveedor",
            "persona_juridica",
        ]

# GET /api/v1/proveedores-empresas/{id}/ 
# consultar un dato en específico
class ProveedorJuridicoDetailSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)
    
    persona_juridica = PersonaJuridicaListSerializer(read_only=True)

    class Meta:
        model = ProveedorJuridico
        fields = [
            "id",
            "proveedor",
            "persona_juridica",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class ProveedorJuridicoBaseSerializer(ModeloBaseSerializer):

    proveedor = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all()
    )

    persona_juridica = serializers.PrimaryKeyRelatedField(
        queryset=PersonaJuridica.objects.all()
    )

    class Meta:
        model = ProveedorJuridico
        fields = (
            "proveedor",
            "persona_juridica",
        )

    def validate_proveedor(self, value):

        if value.tipo != Proveedor.Tipo.NATURAL:
            raise serializers.ValidationError(
                "El proveedor debe ser de tipo jurídico."
            )

        return value
    
# POST /api/v1/proveedores-empresas/ 
# crear un nuevo dato
class ProveedorJuridicoCreateSerializer(ProveedorJuridicoBaseSerializer):
    pass

# PUT / PATCH /api/v1/proveedores-empresas/{id} 
# actualizar completo o parcialmente un elemento
class ProveedorJuridicoUpdateSerializer(ProveedorJuridicoBaseSerializer):
    pass