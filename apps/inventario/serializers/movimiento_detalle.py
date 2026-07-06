from rest_framework import serializers
from ..models.movimiento_detalle import MovimientoDetalle
from ..serializers.movimiento import MovimientoListSerializer
from apps.catalogo.serializers.producto import ProductoListSerializer

# GET /api/v1/movimiento-detalles/ 
# consultar todo los datos
class MovimientoDetalleListSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = MovimientoDetalle
        fields = [
            "id",
            "movimiento",
            "producto",
            "cantidad",
            "precio",
            "descuento",
            "sub_total",
        ]

# GET /api/v1/movimiento-detalle/{id}/ 
# consultar un dato en específico
class MovimientoDetalleDetailSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    producto = ProductoListSerializer(read_only=True)

    class Meta:
        model = MovimientoDetalle
        fields = [
            "id",
            "movimiento",
            "producto",
            "cantidad",
            "precio",
            "descuento",
            "sub_total",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/movimiento-detalle/ 
# crear un nuevo dato
class MovimientoDetalleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoDetalle
        fields = [
            "movimiento",
            "producto",
            "cantidad",
            "precio",
            "descuento",
            "sub_total",
        ]

# PUT / PATCH /api/v1/movimiento-detalle/{id} 
# actualizar completo o parcialmente un elemento
class MovimientoDetalleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoDetalle
        fields = [
            "movimiento",
            "producto",
            "cantidad",
            "precio",
            "descuento",
            "sub_total",
        ]