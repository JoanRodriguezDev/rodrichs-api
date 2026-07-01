from rest_framework import serializers
from ..models.cliente_juridico import ClienteJuridico
from ..models.cliente import Cliente
from ..models.persona_juridica import PersonaJuridica
from ..serializers.cliente import ClienteListSerializer
from ..serializers.persona_juridica import PersonaJuridicaListSerializer

# GET /api/v1/clientes-empresas/ 
# consultar todo los datos
class ClienteJuridicoListSerializer(serializers.ModelSerializer):
    cliente = ClienteListSerializer(read_only=True)
    persona_juridica = PersonaJuridicaListSerializer(read_only=True)

    class Meta:
        model = ClienteJuridico
        fields = (
            'id',
            'cliente',
            'persona_juridica',
        )

# GET /api/v1/clientes-empresas/{id}/ 
# consultar un dato en específico
class ClienteJuridicoDetailSerializer(serializers.ModelSerializer):
    cliente = ClienteListSerializer(read_only=True)
    persona_juridica = PersonaJuridicaListSerializer(read_only=True)

    class Meta:
        model = ClienteJuridico
        fields = (
            'id',
            'cliente',
            'persona_juridica',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/clientes-empresas/ 
# crear un nuevo dato
class ClienteJuridicoCreateSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all()
    )

    persona_juridica = serializers.PrimaryKeyRelatedField(
        queryset=PersonaJuridica.objects.all()
    )

    class Meta:
        model = ClienteJuridico
        fields = (
            'cliente',
            'persona_juridica',
        )

# PUT / PATCH /api/v1/clientes-empresas/{id} 
# actualizar completo o parcialmente un elemento
class ClienteJuridicoUpdateSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all()
    )

    persona_juridica = serializers.PrimaryKeyRelatedField(
        queryset=PersonaJuridica.objects.all()
    )

    class Meta:
        model = ClienteJuridico
        fields = (
            'cliente',
            'persona_juridica',
        )