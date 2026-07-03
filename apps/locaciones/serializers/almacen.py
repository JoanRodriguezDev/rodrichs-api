from rest_framework import serializers
from ..models.almacen import Almacen
from ..serializers.sucursal import SucursalListSerializer

# GET /api/v1/almacenes/ 
# consultar todo los datos
class AlmacenListSerializer(serializers.ModelSerializer):
    sucursal = SucursalListSerializer(read_only=True)

    class Meta:
        model = Almacen
        fields = (
            'id',
            'nombre',
            'tipo',
            'sucursal',
        )

# GET /api/v1/almacenes/{id}/ 
# consultar un dato en específico
class AlmacenDetailSerializer(serializers.ModelSerializer):
    sucursal = SucursalListSerializer(read_only=True)

    class Meta:
        model = Almacen
        fields = (
            'id',
            'nombre',
            'tipo',
            'sucursal',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/almacenes/ 
# crear un nuevo dato
class AlmacenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = (
            'nombre',
            'tipo',
            'sucursal',
        )

# PUT / PATCH /api/v1/almacenes/{id} 
# actualizar completo o parcialmente un elemento
class AlmacenUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = (
            'nombre',
            'tipo',
            'sucursal',
        )