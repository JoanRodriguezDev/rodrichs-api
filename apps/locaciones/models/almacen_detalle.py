from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .almacen import Almacen


class AlmacenDetalleStock(ModeloBase):

    almacen = models.ForeignKey(
        Almacen,
        verbose_name="Almacén",
        on_delete=models.PROTECT,
        related_name="detalles",
        help_text="Almacén donde se encuentra registrado el stock del producto."
    )

    producto = models.ForeignKey(
        "catalogo.Producto",
        verbose_name="Producto",
        on_delete=models.PROTECT,
        related_name="almacen_detalles",
        help_text="Producto al que corresponde el stock registrado."
    )

    cantidad = models.PositiveIntegerField(
        verbose_name="Cantidad",
        default=0,
        help_text="Cantidad disponible del producto en el almacén."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "almacen_detalle"
        ordering = ["cantidad"]
        verbose_name = "Almacén Detalle"
        verbose_name_plural = "Almacén Detalles"
        constraints = [
            models.UniqueConstraint(
                fields=["almacen", "producto"],
                name="uq_almacen_producto"
            )
        ]

    def __str__(self):
        return f"{self.producto} - {self.almacen} - {self.cantidad}"