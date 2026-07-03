from rest_framework import serializers
from ..models.caja_detalle import CajaDetalle
from ..models.caja import Caja
from ..serializers.caja import CajaListSerializer
from apps.usuarios.serializers.usuario import UsuarioListSerializer

# GET /api/v1/caja-detalles/ 
# consultar todo los datos
class CajaDetalleListSerializer(serializers.ModelSerializer):
    caja = CajaListSerializer(read_only=True)

    usuario = UsuarioListSerializer(read_only=True)

    class Meta:
        model = CajaDetalle
        fields = (
            'id',
            'caja',
            'usuario',
            'fecha_apertura',
            'monto_inicial',
        )

# GET /api/v1/caja-detalles/{id}/ 
# consultar un dato en específico
class CajaDetalleDetailSerializer(serializers.ModelSerializer):
    caja = CajaListSerializer(read_only=True)

    usuario = UsuarioListSerializer(read_only=True)

    class Meta:
        model = CajaDetalle
        fields = (
            'id',
            'caja',
            'usuario',
            'fecha_apertura',
            'monto_inicial',
            'monto_final',
            'fecha_cierre',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/caja-detalles/ 
# crear un nuevo dato
class CajaDetalleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CajaDetalle
        fields = (
            'caja',
            'usuario',
            'fecha_apertura',
            'monto_inicial',
            'monto_final',
            'fecha_cierre',
        )

# PUT / PATCH /api/v1/caja-detalles/{id} 
# actualizar completo o parcialmente un elemento
class CajaDetalleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CajaDetalle
        fields = (
            'caja',
            'usuario',
            'fecha_apertura',
            'monto_inicial',
            'monto_final',
            'fecha_cierre',
        )