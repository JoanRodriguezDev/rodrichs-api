from rest_framework import serializers
from ..models.movimiento import Movimiento
from apps.usuarios.serializers.usuario import UsuarioListSerializer

# GET /api/v1/movimientos/ 
# consultar todo los datos
class MovimientoListSerializer(serializers.ModelSerializer):
    usuario = UsuarioListSerializer(read_only=True)

    class Meta:
        model = Movimiento
        fields = (
            'id',
            'tipo',
            'fecha',
            'usuario',
        )

# GET /api/v1/movimientos/{id}/ 
# consultar un dato en específico
class MovimientoDetailSerializer(serializers.ModelSerializer):
    usuario = UsuarioListSerializer(read_only=True)

    class Meta:
        model = Movimiento
        fields = (
            'id',
            'tipo',
            'fecha',
            'observacion',
            'usuario',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/movimientos/ 
# crear un nuevo dato
class MovimientoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = (
            'tipo',
            'fecha',
            'observacion',
            'usuario',
        )

# PUT / PATCH /api/v1/movimientos/{id} 
# actualizar completo o parcialmente un elemento
class MovimientoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = (
            'tipo',
            'fecha',
            'observacion',
            'usuario',
        )