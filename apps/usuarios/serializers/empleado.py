from rest_framework import serializers
from ..models.empleado import Empleado
from apps.personas.models.persona_natural import PersonaNatural
from apps.personas.serializers.persona_natural import PersonaNaturalListSerializer

# GET /api/v1/empleado/ 
# consultar todo los datos
class EmpleadoListSerializer(serializers.ModelSerializer):
    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = Empleado
        fields = (
            'id',
            'sueldo',
            'estado',
            'persona_natural',
        )

# GET /api/v1/empleado/{id}/ 
# consultar un dato en específico
class EmpleadoDetailSerializer(serializers.ModelSerializer):
    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = Empleado
        fields = (
            'id',
            'sueldo',
            'estado',
            'fecha_contratacion',
            'fecha_termino',
            'direccion',
            'fecha_nacimiento',
            'persona_natural',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/empleado/ 
# crear un nuevo dato
class EmpleadoCreateSerializer(serializers.ModelSerializer):
    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = Empleado
        fields = (
            'sueldo',
            'estado',
            'fecha_contratacion',
            'fecha_termino',
            'direccion',
            'fecha_nacimiento',
            'persona_natural',
        )

# PUT / PATCH /api/v1/empleado/{id} 
# actualizar completo o parcialmente un elemento
class EmpleadoUpdateSerializer(serializers.ModelSerializer):
    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = Empleado
        fields = (
            'sueldo',
            'estado',
            'fecha_contratacion',
            'fecha_termino',
            'direccion',
            'fecha_nacimiento',
            'persona_natural',
        )