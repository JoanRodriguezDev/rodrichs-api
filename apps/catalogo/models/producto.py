from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .categoria import Categoria

class Producto(ModeloBase):

    class TiposUnidadMedida(models.TextChoices):
        PAR = "PR", "Par"
        METRO = "M", "Metro"
        YARDA = "YD", "Yarda"
        PIE_CUADRADO = "SQ FT", "Pie cuadrado"
        UNIDAD = "U", "Unidad"
        PIEZA = "PC", "Pieza"

    nombre = models.CharField(
        verbose_name="Nombre del producto",
        max_length=60,
        help_text="Nombre comercial con el que se identifica el producto dentro del sistema."
    )

    descripcion = models.CharField(
        verbose_name="Descripción del producto",
        max_length=255,
        blank=True,
        help_text="Descripción opcional con información adicional sobre las características del producto."
    )

    codigo = models.CharField(
        verbose_name="Código del producto",
        max_length=50,
        unique=True,
        help_text="Código único utilizado para identificar el producto en el sistema (código interno, SKU o código de barras)."
    )

    tamanio = models.CharField(
        verbose_name="Tamaño",
        max_length=20,
        blank=True,
        help_text="Tamaño o medida del producto, cuando aplique (ej.: 38, M, XL, 42)."
    )

    color = models.CharField(
        verbose_name="Color",
        max_length=20,
        blank=True,
        help_text="Color principal del producto."
    )

    unidad_medida = models.CharField(
        verbose_name="Unidad de medida",
        max_length=15,
        choices=TiposUnidadMedida.choices,
        default=TiposUnidadMedida.UNIDAD,
        help_text="Unidad de medida utilizada para controlar el inventario y realizar las operaciones de compra y venta."
    )

    precio_costo = models.DecimalField(
        verbose_name="Precio de costo",
        max_digits=12,
        decimal_places=2,
        help_text="Costo de adquisición o fabricación del producto."
    )

    precio_venta = models.DecimalField(
        verbose_name="Precio de venta",
        max_digits=12,
        decimal_places=2,
        help_text="Precio al que se comercializa el producto."
    )

    stock_minimo = models.PositiveIntegerField(
        verbose_name="Stock mínimo",
        default=0,
        help_text="Cantidad mínima permitida en inventario antes de generar una alerta de reposición."
    )

    foto = models.ImageField(
        verbose_name="Imagen del producto",
        upload_to="productos/",
        blank=True,
        null=True,
        help_text="Imagen representativa del producto."
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        verbose_name="Categoría",
        related_name="productos",
        help_text="Categoría a la que pertenece el producto."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "producto"
        ordering = ["nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"