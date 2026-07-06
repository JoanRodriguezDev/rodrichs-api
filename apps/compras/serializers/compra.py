from rest_framework import serializers
from ..models.compra import Compra
from apps.personas.serializers.proveedor import ProveedorListSerializer
from apps.inventario.models.movimiento import Movimiento
from apps.inventario.serializers.movimiento import MovimientoListSerializer

# GET /api/v1/compras/ 
# consultar todo los datos
class CompraListSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)

    movimiento = MovimientoListSerializer(read_only=True)

    class Meta:
        model = Compra
        fields = [
            "id",
            "fecha",
            "total",
            "estado",
            "proveedor",
            "movimiento",
        ]

# GET /api/v1/compraso/{id}/ 
# consultar un dato en específico
class CompraDetailSerializer(serializers.ModelSerializer):
    proveedor = ProveedorListSerializer(read_only=True)

    movimiento = MovimientoListSerializer(read_only=True)

    class Meta:
        model = Compra
        fields = [
            "id",
            "fecha",
            "total",
            "estado",
            "proveedor",
            "movimiento",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/compras/ 
# crear un nuevo dato
class CompraCreateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )

    class Meta:
        model = Compra
        fields = [
            "fecha",
            "total",
            "estado",
            "proveedor",
            "movimiento",
        ]
        
# PUT / PATCH /api/v1/compras/{id} 
# actualizar completo o parcialmente un elemento
class CompraUpdateSerializer(serializers.ModelSerializer):
    movimiento = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all()
    )
    
    class Meta:
        model = Compra
        fields = [
            "fecha",
            "total",
            "estado",
            "proveedor",
            "movimiento",
        ]