from rest_framework import serializers
from ..models.proveedor import Proveedor
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/proveedores/ 
# consultar todo los datos
class ProveedorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            "id",
            "tipo",
        ]

# GET /api/v1/proveedores/{id}/ 
# consultar un dato en específico
class ProveedorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            "id",
            "tipo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class ProveedorBaseSerializer(ModeloBaseSerializer):

    class Meta:
        model = Proveedor
        fields = [
            "tipo",
        ]

# POST /api/v1/proveedores/ 
# crear un nuevo dato
class ProveedorCreateSerializer(ProveedorBaseSerializer):
    pass

# PUT / PATCH /api/v1/proveedores/{id} 
# actualizar completo o parcialmente un elemento
class ProveedorUpdateSerializer(ProveedorBaseSerializer):
    pass