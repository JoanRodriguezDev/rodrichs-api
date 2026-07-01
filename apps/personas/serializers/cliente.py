from rest_framework import serializers
from ..models.cliente import Cliente

# GET /api/v1/clientes/ 
# consultar todo los datos
class ClienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'tipo',
        )

# GET /api/v1/clientes/{id}/ 
# consultar un dato en específico
class ClienteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/clientes/ 
# crear un nuevo dato
class ClienteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'tipo',
        )

# PUT / PATCH /api/v1/clientes/{id} 
# actualizar completo o parcialmente un elemento
class ClienteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'tipo',
        )