from rest_framework import serializers
from ..models.persona_natural import PersonaNatural
from ..serializers.pais import PaisListSerializer
from ..serializers.tipo_documento_identidad import TipoDocumentoIdentidadListSerializer

# GET /api/v1/personas/ 
# consultar todo los datos
class PersonaNaturalListSerializer(serializers.ModelSerializer):
    pais = PaisListSerializer(read_only=True)
    tipo_documento = TipoDocumentoIdentidadListSerializer(read_only=True)
    class Meta:
        model = PersonaNatural
        fields = [
            "id",
            "nombres",
            "apellido_paterno",
            "apellido_materno",
            "numero_documento",
            "numero_celular",
            "email",
            "pais",
            "tipo_documento",
        ]

# GET /api/v1/personas/ 
# consultar todo los datos
class PersonaNaturalDetailtSerializer(serializers.ModelSerializer):
    pais = PaisListSerializer(read_only=True)
    tipo_documento = TipoDocumentoIdentidadListSerializer(read_only=True)
    class Meta:
        model = PersonaNatural
        fields = [
            "id",
            "nombres",
            "apellido_paterno",
            "apellido_materno",
            "numero_documento",
            "numero_celular",
            "email",
            "pais",
            "tipo_documento",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

# POST /api/v1/personas/ 
# crear un nuevo dato
class PersonaNaturalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = [
            "nombres",
            "apellido_paterno",
            "apellido_materno",
            "numero_documento",
            "numero_celular",
            "email",
            "pais",
            "tipo_documento",
        ]

# PUT / PATCH /api/v1/personas/{id} 
# actualizar completo o parcialmente un elemento
class PersonaNaturalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = [
            "nombres",
            "apellido_paterno",
            "apellido_materno",
            "numero_documento",
            "numero_celular",
            "email",
            "pais",
            "tipo_documento",
        ]