from rest_framework import serializers
from ..models.kardex import Kardex
from ..serializers.movimiento import MovimientoListSerializer
from apps.catalogo.serializers.producto import ProductoListSerializer
from apps.locaciones.serializers.almacen import AlmacenListSerializer

# GET /api/v1/kardex/ 
# consultar todo los datos
class KardexListSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    almacen = AlmacenListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = Kardex
        fields = (
            'id',
            'stock_anterior',
            'stock_nuevo',
            'movimiento',
            'almacen',
            'producto',
        )

# GET /api/v1/kardex/{id}/ 
# consultar un dato en específico
class KardexDetailSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    almacen = AlmacenListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = Kardex
        fields = (
            'id',
            'stock_anterior',
            'stock_nuevo',
            'entrada',
            'salida',
            'movimiento',
            'almacen',
            'producto',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/kardex/ 
# crear un nuevo dato
class KardexCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kardex
        fields = (
            'stock_anterior',
            'stock_nuevo',
            'entrada',
            'salida',
            'movimiento',
            'almacen',
            'producto',
        )

# PUT / PATCH /api/v1/kardex/{id} 
# actualizar completo o parcialmente un elemento
class KardexUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kardex
        fields = (
            'stock_anterior',
            'stock_nuevo',
            'entrada',
            'salida',
            'movimiento',
            'almacen',
            'producto',
        )