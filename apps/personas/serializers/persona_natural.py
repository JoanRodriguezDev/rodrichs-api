from rest_framework import serializers
from ..models.persona_natural import PersonaNatural
from ..serializers.pais import PaisListSerializer
from ..serializers.tipo_documento_identidad import TipoDocumentoIdentidadListSerializer
from apps.core.serializers import ModeloBaseSerializer

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
class PersonaNaturalDetailSerializer(serializers.ModelSerializer):
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

class PersonaNaturalBaseSerializer(ModeloBaseSerializer):

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

        def validate(self, attrs):

            pais = self.obtener_valor(attrs, "pais")
            tipo_documento = self.obtener_valor(attrs, "tipo_documento")
            numero_documento = self.obtener_valor(attrs, "numero_documento")
            numero_celular = self.obtener_valor(attrs, "numero_celular")

            self.validar_longitud_celular(
                pais,
                numero_celular,
            )

            self.validar_numero_documento(
                tipo_documento,
                numero_documento,
            )

            return attrs
        
        def validate_nombres(self, value):
            return self.normalizar_string(value)
        
        def validate_apellido_paterno(self, value):
            return self.normalizar_string(value)

        def validate_apellido_materno(self, value):
            return self.normalizar_string(value)
        
        def validate_email(self, value):
            return self.normalizar_lower(value)
        
        def validate_numero_documento(self, value):
            return self.normalizar_upper(value)
        
        def validate_numero_celular(self, value):
            return self.normalizar_string(value)
        

        
# POST /api/v1/personas/ 
# crear un nuevo dato
class PersonaNaturalCreateSerializer(PersonaNaturalBaseSerializer):
    pass

# PUT / PATCH /api/v1/personas/{id} 
# actualizar completo o parcialmente un elemento
class PersonaNaturalUpdateSerializer(PersonaNaturalBaseSerializer):
    pass