from rest_framework import serializers
from ..models.producto import Producto
from ..models.categoria import Categoria
from ..serializers.categoria import CategoriaListSerializer

# GET /api/v1/productos/ 
# consultar todo los datos
class ProductoListSerializer(serializers.ModelSerializer):
    categoria = CategoriaListSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'codigo',
            'precio_venta',
            'stock_minimo',
            'categoria',
        )

# GET /api/v1/productos/{id}/ 
# consultar un dato en específico
class ProductoDetailSerializer(serializers.ModelSerializer):
    categoria = CategoriaListSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'descripcion',
            'codigo',
            'tamanio',
            'color',
            'unidad_medida',
            'precio_costo',
            'precio_venta',
            'stock_minimo',
            'foto',
            'categoria',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

# POST /api/v1/productos/ 
# crear un nuevo dato
class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'descripcion',
            'codigo',
            'tamanio',
            'color',
            'unidad_medida',
            'precio_costo',
            'precio_venta',
            'stock_minimo',
            'foto',
            'categoria',
        )

# PUT / PATCH /api/v1/productos/{id} 
# actualizar completo o parcialmente un elemento
class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'descripcion',
            'codigo',
            'tamanio',
            'color',
            'unidad_medida',
            'precio_costo',
            'precio_venta',
            'stock_minimo',
            'foto',
            'categoria',
        )