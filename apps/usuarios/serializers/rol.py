from rest_framework import serializers
from ..models.rol import Rol
from ..models.permiso import Permiso
from ..serializers.permiso import PermisoListSerializer

# GET /api/v1/roles/ 
# consultar todo los datos
class RolListSerializer(serializers.ModelSerializer):
    permisos = PermisoListSerializer(many=True, read_only=True)

    class Meta:
        model = Rol
        fields = [
            "id",
            "nombre",
            "permisos",
        ]

# GET /api/v1/roles/{id}/ 
# consultar un dato en específico
class RolDetailSerializer(serializers.ModelSerializer):
    permisos = PermisoListSerializer(many=True, read_only=True)

    class Meta:
        model = Rol
        fields = [
            "id",
            "nombre",
            "permisos",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/roles/ 
# crear un nuevo dato
class RolCreateSerializer(serializers.ModelSerializer):
    permisos = serializers.PrimaryKeyRelatedField(
        queryset=Permiso.objects.all(),
        many=True
    )

    class Meta:
        model = Rol
        fields = [
            "nombre",
            "permisos",
        ]

# PUT / PATCH /api/v1/roles/{id} 
# actualizar completo o parcialmente un elemento
class RolUpdateSerializer(serializers.ModelSerializer):
    permisos = serializers.PrimaryKeyRelatedField(
        queryset=Permiso.objects.all(),
        many=True
    )

    class Meta:
        model = Rol
        fields = [
            "nombre",
            "permisos",
        ]