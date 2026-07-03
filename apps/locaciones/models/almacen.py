from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .sucursal import Sucursal

class Almacen(ModeloBase):

    class Tipo(models.TextChoices):
        PRINCIPAL = "principal", "Almacén principal"
        TIENDA = "tienda", "Tienda"

    nombre = models.CharField(
        verbose_name="Nombre del almacén",
        max_length=60,
        help_text="Nombre con el que se identifica el almacén dentro del sistema."
    )

    tipo = models.CharField(
        verbose_name="Tipo de almacén",
        max_length=25,
        choices=Tipo.choices,
        help_text="Tipo de almacén según su función dentro de la empresa, como almacén principal o tienda."
    )

    sucursal = models.ForeignKey(
        Sucursal,
        verbose_name="Sucursal",
        on_delete=models.PROTECT,
        related_name="almacenes",
        help_text="Sucursal a la que pertenece el almacén."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "almacen"
        ordering = ["nombre"]
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"
        constraints = [
            models.UniqueConstraint(
                fields=["sucursal", "nombre"],
                name="uq_almacen_sucursal_nombre"
            )
        ]

    def __str__(self):
        return f"{self.nombre} - {self.sucursal}"