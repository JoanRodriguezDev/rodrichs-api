from rest_framework import serializers
from ..models.tipo_documento_identidad import TipoDocumentoIdentidad

# GET /api/v1/tipo-documento/ 
# consultar todo los datos
class TipoDocumentoIdentidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = (
            'id',
            'codigo',
            'nombre',
            'descripcion',
        )

# GET /api/v1/tipo-documento/{id}/ 
# consultar un dato en específico
class TipoDocumentoIdentidadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = (
            'id',
            'codigo',
            'nombre',
            'descripcion',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/tipo-documento/ 
# crear un nuevo dato
class TipoDocumentoIdentidadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = (
            'codigo',
            'nombre',
            'descripcion',
        )

# PUT / PATCH /api/v1/tipo-documento/{id} 
# actualizar completo o parcialmente un elemento
class TipoDocumentoIdentidadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = (
            'codigo',
            'nombre',
            'descripcion',
        )


# GET /api/v1/tipo-documento/ 
# consultar todo los datos

# GET /api/v1/tipo-documento/{id}/ 
# consultar un dato en específico

# POST /api/v1/tipo-documento/ 
# crear un nuevo dato

# PUT / PATCH /api/v1/tipo-documento/{id} 
# actualizar completo o parcialmente un elemento