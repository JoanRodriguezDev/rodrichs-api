from rest_framework import serializers
from ..models.almacen_detalle import AlmacenDetalleStock
from ..serializers.almacen import AlmacenListSerializer
from apps.catalogo.serializers.producto import ProductoListSerializer

# GET /api/v1/almacen-detalles/ 
# consultar todo los datos
class AlmacenDetalleListSerializer(serializers.ModelSerializer):
    almacen = AlmacenListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = AlmacenDetalleStock
        fields = (
            'id',
            'almacen',
            'producto',
            'cantidad',
        )

# GET /api/v1/almacen-detalles/{id}/ 
# consultar un dato en específico
class AlmacenDetalleDetailSerializer(serializers.ModelSerializer):
    almacen = AlmacenListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = AlmacenDetalleStock
        fields = (
            'id',
            'almacen',
            'producto',
            'cantidad',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/almacen-detalles/ 
# crear un nuevo dato
class AlmacenDetalleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlmacenDetalleStock
        fields = (
            'id',
            'almacen',
            'producto',
            'cantidad',
        )

# PUT / PATCH /api/v1/almacen-detalles/{id} 
# actualizar completo o parcialmente un elemento
class AlmacenDetalleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlmacenDetalleStock
        fields = (
            'id',
            'almacen',
            'producto',
            'cantidad',
        )