from rest_framework import serializers
from ..models.usuario import Usuario
from ..models.rol import Rol
from ..models.empleado import Empleado
from ..serializers.rol import RolListSerializer
from ..serializers.empleado import EmpleadoListSerializer
from django.contrib.auth.password_validation import validate_password

# GET /api/v1/usuarios/ 
# consultar todo los datos
class UsuarioListSerializer(serializers.ModelSerializer):
    rol = RolListSerializer(read_only=True)

    empleado = EmpleadoListSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = [
            "id",
            "username",
            "email",
            "rol",
            "empleado",
        ]

# GET /api/v1/usuarios/{id}/ 
# consultar un dato en específico
class UsuarioDetailSerializer(serializers.ModelSerializer):
    rol = RolListSerializer(read_only=True)

    empleado = EmpleadoListSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = [
            "id",
            "username",
            "email",
            "rol",
            "empleado",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/usuarios/ 
# crear un nuevo dato
class UsuarioCreateSerializer(serializers.ModelSerializer):
    empleado = serializers.PrimaryKeyRelatedField(
        queryset=Empleado.objects.all()
    )

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "password",
            "rol",
            "empleado",
        ]
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Usuario.objects.create_user(
            password=password,
            **validated_data
        )
        return user
    
# Serializer que sirve para heredar el método update y poder actualizar la contraseña del usuario de manera segura.
class UsuarioPasswordMixin:

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance
    
# PUT / PATCH /api/v1/usuarios/{id} 
# actualizar completo o parcialmente un elemento
class UsuarioUpdateSerializer(UsuarioPasswordMixin,serializers.ModelSerializer):
    empleado = serializers.PrimaryKeyRelatedField(
        queryset=Empleado.objects.all()
    )

    password = serializers.CharField(
        write_only=True,
        required=False,
        validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "password",
            "rol",
            "empleado",
        ]

# PUT / PATCH /api/v1/usuarios/{id} --- PERO SOLO PARA PERFIL DE USUARIO
# actualizar completo o parcialmente un elemento en PERFIL DE USUARIO
class UsuarioPerfilSerializer(UsuarioPasswordMixin,serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = [
            "email",
            "password",
        ]