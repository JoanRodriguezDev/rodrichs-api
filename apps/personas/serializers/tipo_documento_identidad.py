from rest_framework import serializers
from ..models.tipo_documento_identidad import TipoDocumentoIdentidad
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/tipo-documento/ 
# consultar todo los datos
class TipoDocumentoIdentidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = [
            "id",
            "codigo",
            "nombre",
            "descripcion",
        ]

# GET /api/v1/tipo-documento/{id}/ 
# consultar un dato en específico
class TipoDocumentoIdentidadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = [
            "id",
            "codigo",
            "nombre",
            "descripcion",
            "longitud",
            "tipo_validacion",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class TipoDocumentoIdentidadBaseSerializer(ModeloBaseSerializer):

        class Meta:
            model = TipoDocumentoIdentidad
            fields = [
                "codigo",
                "nombre",
                "descripcion",
                "longitud",
                "tipo_validacion",
            ]

        def validate_codigo(self, value):
            return self.normalizar_string(value)

        def validate_nombre(self, value):
            value = self.normalizar_string(value)

            self.validar_unico_sin_distincion_de_mayusculas_y_minusculas(
                TipoDocumentoIdentidad,
                "nombre",
                value,
            )

            return value

        def validate_descripcion(self, value):
            return self.normalizar_string(value)

# POST /api/v1/tipo-documento/ 
# crear un nuevo dato
class TipoDocumentoIdentidadCreateSerializer(TipoDocumentoIdentidadBaseSerializer):
    pass

# PUT / PATCH /api/v1/tipo-documento/{id} 
# actualizar completo o parcialmente un elemento
class TipoDocumentoIdentidadUpdateSerializer(TipoDocumentoIdentidadBaseSerializer):
    pass