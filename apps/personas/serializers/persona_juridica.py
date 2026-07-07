from rest_framework import serializers
from apps.core.serializers import ModeloBaseSerializer
from ..models.persona_juridica import PersonaJuridica

# GET /api/v1/empresas/ 
# consultar todo los datos
class PersonaJuridicaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "id",
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
        ]

# GET /api/v1/empresas/{id}/ 
# consultar un dato en específico
class PersonaJuridicaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = [
            "id",
            "ruc",
            "razon_social",
            "estado",
            "direccion",
            "condicion",
            "departamento",
            "provincia",
            "distrito",
            "ubigeo_sunat",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

class PersonaJuridicaBaseSerializer(ModeloBaseSerializer):

        class Meta:
            model = PersonaJuridica
            fields = [
                "ruc",
                "razon_social",
                "estado",
                "direccion",
                "condicion",
                "departamento",
                "provincia",
                "distrito",
                "ubigeo_sunat",
            ]
        
        def validate_ruc(self, value):
            return self.normalizar_string(value)
        
        def validate_razon_social(self, value):
            value = self.normalizar_string(value)

            self.validar_unico_sin_distincion_de_mayusculas_y_minusculas(
                PersonaJuridica,
                "razon_social",
                value,
            )

            return value
        
        def validate_direccion(self, value):
            return self.normalizar_string(value)
        
        def validate_departamento(self, value):
            return self.normalizar_string(value)
        
        def validate_provincia(self, value):
            return self.normalizar_string(value)
        
        def validate_distrito(self, value):
            return self.normalizar_string(value)
        
        def validate_ubigeo_sunat(self, value):
            return self.normalizar_string(value)

        
        
# POST /api/v1/empresas/ 
# crear un nuevo dato
class PersonaJuridicaCreateSerializer(PersonaJuridicaBaseSerializer):
    pass

# PUT / PATCH /api/v1/empresas/{id} 
# actualizar completo o parcialmente un elemento
class PersonaJuridicaUpdateSerializer(PersonaJuridicaBaseSerializer):
    pass