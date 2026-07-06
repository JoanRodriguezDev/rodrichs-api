from rest_framework import serializers
from ..models.persona_juridica import PersonaJuridica

# GET /api/v1/empresas/ 
# consultar todo los datos
class PersonaJuridicaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "id",
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
        ]

# GET /api/v1/empresas/{id}/ 
# consultar un dato en específico
class PersonaJuridicaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "id",
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/empresas/ 
# crear un nuevo dato
class PersonaJuridicaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
        ]

# PUT / PATCH /api/v1/empresas/{id} 
# actualizar completo o parcialmente un elemento
class PersonaJuridicaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
        ]