from rest_framework import serializers
from ..models.cliente_natural import ClienteNatural
from ..models.cliente import Cliente
from ..models.persona_natural import PersonaNatural
from ..serializers.cliente import ClienteListSerializer
from ..serializers.persona_natural import PersonaNaturalListSerializer
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/clientes-naturales/ 
# consultar todo los datos
class ClienteNaturalListSerializer(serializers.ModelSerializer):
    cliente = ClienteListSerializer(read_only=True)
    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = ClienteNatural
        fields = [
            "id",
            "cliente",
            "persona_natural",
        ]

# GET /api/v1/clientes-naturales/{id}/ 
# consultar un dato en específico
class ClienteNaturalDetailSerializer(serializers.ModelSerializer):
    cliente = ClienteListSerializer(read_only=True)
    persona_natural = PersonaNaturalListSerializer(read_only=True)

    class Meta:
        model = ClienteNatural
        fields = [
            "id",
            "cliente",
            "persona_natural",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class ClienteNaturalBaseSerializer(ModeloBaseSerializer):

    cliente = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all()
    )

    persona_natural = serializers.PrimaryKeyRelatedField(
        queryset=PersonaNatural.objects.all()
    )

    class Meta:
        model = ClienteNatural
        fields = (
            "cliente",
            "persona_natural",
        )

    def validate_cliente(self, value):

        if value.tipo != Cliente.Tipo.NATURAL:
            raise serializers.ValidationError(
                "El cliente debe ser de tipo natural."
            )

        return value
    
# POST /api/v1/clientes-naturales/ 
# crear un nuevo dato
class ClienteNaturalCreateSerializer(ClienteNaturalBaseSerializer):
    pass

# PUT / PATCH /api/v1/clientes-naturales/{id} 
# actualizar completo o parcialmente un elemento
class ClienteNaturalUpdateSerializer(ClienteNaturalBaseSerializer):
    pass