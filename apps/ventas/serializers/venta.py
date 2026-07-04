from rest_framework import serializers
from ..models.venta import Venta
from apps.personas.serializers.cliente import ClienteListSerializer
from apps.caja.serializers.caja import CajaListSerializer
from apps.inventario.models.movimiento import Movimiento
from apps.inventario.serializers.movimiento import MovimientoListSerializer

# GET /api/v1/ventas/ 
# consultar todo los datos
class VentaListSerializer(serializers.ModelSerializer):
    caja = CajaListSerializer(read_only=True)

    cliente = ClienteListSerializer(read_only=True)

    movimiento = MovimientoListSerializer(read_only=True)

    class Meta:
        model = Venta
        fields = (
            'id',
            'fecha',
            'total',
            'estado',
            'caja',
            'cliente',
            'movimiento',
        )

# GET /api/v1/ventas/{id}/ 
# consultar un dato en específico
class VentaDetailSerializer(serializers.ModelSerializer):
    caja = CajaListSerializer(read_only=True)

    cliente = ClienteListSerializer(read_only=True)

    movimiento = MovimientoListSerializer(read_only=True)

    class Meta:
        model = Venta
        fields = (
            'id',
            'fecha',
            'total',
            'estado',
            'caja',
            'cliente',
            'movimiento',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/ventas/ 
# crear un nuevo dato
class VentaCreateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )

    class Meta:
        model = Venta
        fields = (
            'fecha',
            'total',
            'estado',
            'caja',
            'cliente',
            'movimiento',
        )

# PUT / PATCH /api/v1/ventas/{id} 
# actualizar completo o parcialmente un elemento
class VentaUpdateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )

    class Meta:
        model = Venta
        fields = (
            'fecha',
            'total',
            'estado',
            'caja',
            'cliente',
            'movimiento',
        )