from rest_framework import serializers
from ..models.permiso import Permiso

# GET /api/v1/permisos/ 
# consultar todo los datos
class PermisoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = (
            'id',
            'codigo',
            'descripcion',
        )

# GET /api/v1/permisos/{id}/ 
# consultar un dato en específico
class PermisoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = (
            'id',
            'codigo',
            'descripcion',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/permisos/ 
# crear un nuevo dato
class PermisoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = (
            'codigo',
            'descripcion',
        )
# PUT / PATCH /api/v1/permisos/{id} 
# actualizar completo o parcialmente un elemento
class PermisoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = (
            'codigo',
            'descripcion',
        )