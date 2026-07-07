from rest_framework import serializers
from ..models.pais import Pais
from apps.core.serializers import ModeloBaseSerializer

# GET /api/v1/pais/ 
# consultar todo los datos
class PaisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "id",
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
        ]

# GET /api/v1/pais/ 
# consultar todo los datos
class PaisDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            "id",
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class PaisBaseSerializer(ModeloBaseSerializer):

    class Meta:
        model = Pais
        fields = [
            "nombre",
            "iso2",
            "iso3",
            "codigo_telefonico",
            "longitud_celular",
        ]

    #Este método sirve para cuando aparezcan reglas de "si A entonces B"
    def validate(self, attrs):
        return attrs

    def validate_nombre(self, value):
        value = self.normalizar_string(value)

        self.validar_unico_sin_distincion_de_mayusculas_y_minusculas(
            Pais,
            "nombre",
            value,
        )

        return value

    def validate_iso2(self, value):
        return self.normalizar_upper(value)

    def validate_iso3(self, value):
        return self.normalizar_upper(value)

    def validate_codigo_telefonico(self, value):
        return self.normalizar_string(value)

# POST /api/v1/pais/ 
# crear un nuevo dato
class PaisCreateSerializer(PaisBaseSerializer):
    pass

# PUT / PATCH /api/v1/pais/{id} 
# actualizar completo o parcialmente un elemento
class PaisUpdateSerializer(PaisBaseSerializer):
    pass
