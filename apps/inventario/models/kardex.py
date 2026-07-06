from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .movimiento import Movimiento

class Kardex(ModeloBase):

    stock_anterior = models.IntegerField(
        verbose_name="Stock anterior",
        help_text="Cantidad disponible del producto en el almacén antes de registrar el movimiento."
    )

    stock_nuevo = models.IntegerField(
        verbose_name="Stock nuevo",
        help_text="Cantidad disponible del producto en el almacén después de registrar el movimiento."
    )

    entrada = models.PositiveIntegerField(
        verbose_name="Entrada",
        default=0,
        help_text="Cantidad de unidades que ingresaron al almacén mediante el movimiento."
    )

    salida = models.PositiveIntegerField(
        verbose_name="Salida",
        default=0,
        help_text="Cantidad de unidades que salieron del almacén mediante el movimiento."
    )

    movimiento = models.ForeignKey(
        Movimiento,
        verbose_name="Movimiento",
        on_delete=models.PROTECT,
        related_name="kardex",
        help_text="Movimiento de inventario que originó este registro de kárdex."
    )

    almacen = models.ForeignKey(
        "locaciones.Almacen",
        verbose_name="Almacén",
        on_delete=models.PROTECT,
        related_name="kardex",
        help_text="Almacén donde se produjo el movimiento del producto."
    )

    producto = models.ForeignKey(
        "catalogo.Producto",
        verbose_name="Producto",
        on_delete=models.PROTECT,
        related_name="kardex",
        help_text="Producto al que corresponde este registro del kárdex."
    )
    
    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "kardex"
        ordering = ["-created_at"]
        verbose_name = "Kárdex"
        verbose_name_plural = "Kárdex"
        constraints = [
            models.UniqueConstraint(
                fields=["movimiento", "almacen", "producto"],
                name="uq_kardex_movimiento_almacen_producto"
            )
        ]
    
    def __str__(self):
        return f"{self.movimiento} - {self.producto} - {self.stock_anterior} - {self.stock_nuevo}"