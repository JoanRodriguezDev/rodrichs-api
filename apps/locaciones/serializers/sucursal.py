from rest_framework import serializers
from ..models.sucursal import Sucursal

# GET /api/v1/sucursales/ 
# consultar todo los datos
class SucursalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [
            "id",
            "nombre",
            "direccion",
        ]

# GET /api/v1/sucursales/{id}/ 
# consultar un dato en específico
class SucursalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [
            "id",
            "nombre",
            "direccion",
            "telefono",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/sucursales/ 
# crear un nuevo dato
class SucursalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [
            "nombre",
            "direccion",
            "telefono",
        ]

# PUT / PATCH /api/v1/sucursales/{id} 
# actualizar completo o parcialmente un elemento
class SucursalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [
            "nombre",
            "direccion",
            "telefono",
        ]