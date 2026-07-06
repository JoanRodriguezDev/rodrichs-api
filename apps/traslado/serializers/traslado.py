from rest_framework import serializers
from ..models.traslado import Traslado
from apps.inventario.models.movimiento import Movimiento
from apps.inventario.serializers.movimiento import MovimientoListSerializer
from apps.locaciones.serializers.almacen import AlmacenListSerializer

# GET /api/v1/traslados/ 
# consultar todo los datos
class TrasladoListSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    almacen_origen = AlmacenListSerializer(read_only=True)

    almacen_destino = AlmacenListSerializer(read_only=True)

    class Meta:
        model = Traslado
        fields = [
            "id",
            "fecha",
            "estado",
            "movimiento",
            "almacen_origen",
            "almacen_destino",
        ]

# GET /api/v1/traslados/{id}/ 
# consultar un dato en específico
class TrasladoDetailSerializer(serializers.ModelSerializer):
    movimiento = MovimientoListSerializer(read_only=True)

    almacen_origen = AlmacenListSerializer(read_only=True)

    almacen_destino = AlmacenListSerializer(read_only=True)

    class Meta:
        model = Traslado
        fields = [
            "id",
            "fecha",
            "estado",
            "movimiento",
            "almacen_origen",
            "almacen_destino",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/traslados/ 
# crear un nuevo dato
class TrasladoCreateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )

    class Meta:
        model = Traslado
        fields = [
            "fecha",
            "estado",
            "movimiento",
            "almacen_origen",
            "almacen_destino",
        ]

# PUT / PATCH /api/v1/traslados/{id} 
# actualizar completo o parcialmente un elemento
class TrasladoUpdateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )

    class Meta:
        model = Traslado
        fields = [
            "fecha",
            "estado",
            "movimiento",
            "almacen_origen",
            "almacen_destino",
        ]