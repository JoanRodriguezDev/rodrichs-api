from rest_framework import serializers
from ..models.categoria import Categoria

# GET /api/v1/categorias/ 
# consultar todo los datos
class CategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'nombre',
            'descripcion',
        )

# GET /api/v1/categorias/{id}/ 
# consultar un dato en específico
class CategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'nombre',
            'descripcion',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/categorias/ 
# crear un nuevo dato
class CategoriaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'nombre',
            'descripcion',
        )

# PUT / PATCH /api/v1/categorias/{id} 
# actualizar completo o parcialmente un elemento
class CategoriaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'nombre',
            'descripcion',
        )
