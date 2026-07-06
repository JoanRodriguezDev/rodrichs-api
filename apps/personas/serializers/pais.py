from rest_framework import serializers
from ..models.pais import Pais

# GET /api/v1/pais/ 
# consultar todo los datos
class PaisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "id",
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
        ]

# GET /api/v1/pais/ 
# consultar todo los datos
class PaisDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "id",
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/pais/ 
# crear un nuevo dato
class PaisCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
        ]

# PUT / PATCH /api/v1/pais/{id} 
# actualizar completo o parcialmente un elemento
class PaisUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
        ]
