from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .movimiento import Movimiento

class MovimientoDetalle(ModeloBase):

    movimiento = models.ForeignKey(
        Movimiento,
        verbose_name="Movimiento",
        on_delete=models.PROTECT,
        related_name="detalles",
        help_text="Movimiento de inventario al que pertenece este detalle."
    )

    producto = models.ForeignKey(
        "catalogo.Producto",
        verbose_name="Producto",
        on_delete=models.PROTECT,
        related_name="movimiento_detalles",
        help_text="Producto involucrado en el movimiento de inventario."
    )

    cantidad = models.PositiveIntegerField(
        verbose_name="Cantidad",
        default=0,
        help_text="Cantidad de unidades del producto incluidas en el movimiento."
    )

    precio = models.DecimalField(
        verbose_name="Precio",
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="Precio unitario del producto registrado en el momento del movimiento."
    )

    descuento = models.DecimalField(
        verbose_name="Descuento",
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="Descuento aplicado al producto dentro del movimiento."
    )

    sub_total = models.DecimalField(
        verbose_name="Subtotal",
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="Importe total correspondiente al producto, calculado según la cantidad, el precio unitario y el descuento aplicado."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "movimiento_detalle"
        ordering = ["cantidad"]
        verbose_name = "Movimiento Detalle"
        verbose_name_plural = "Movimiento Detalles"
        constraints = [
            models.UniqueConstraint(
                fields=["movimiento", "producto"],
                name="uq_movimiento_producto"
            )
        ]


    def __str__(self):
        return f"{self.producto} - {self.movimiento} - {self.cantidad}"

