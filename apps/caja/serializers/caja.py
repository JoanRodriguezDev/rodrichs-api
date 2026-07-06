from rest_framework import serializers
from ..models.caja import Caja

# GET /api/v1/cajas/ 
# consultar todo los datos
class CajaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
            "id",
            "nombre",
            "descripcion",
            "estado",
        ]

# GET /api/v1/cajas/{id}/ 
# consultar un dato en específico
class CajaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
            "id",
            "nombre",
            "descripcion",
            "estado",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/cajas/ 
# crear un nuevo dato
class CajaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
            "nombre",
            "descripcion",
            "estado",
        ]

# PUT / PATCH /api/v1/cajas/{id} 
# actualizar completo o parcialmente un elemento
class CajaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
            "nombre",
            "descripcion",
            "estado",
        ]