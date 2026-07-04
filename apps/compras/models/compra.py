from django.db import models
from django.utils import timezone
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager


class Compra(ModeloBase):

    class Estado(models.TextChoices):
        COMPLETADO = "completado", "Compra completada"
        INCOMPLETO = "incompleto", "Compra incompleta"

    fecha = models.DateTimeField(
        verbose_name="Fecha de la compra",
        default=timezone.now,
        help_text="Fecha y hora en que se registró la compra."
    )

    total = models.DecimalField(
        verbose_name="Total de la compra",
        max_digits=12,
        decimal_places=2,
        help_text="Importe total de la compra, considerando todos los productos registrados."
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=20,
        choices=Estado.choices,
        default=Estado.INCOMPLETO,
        help_text="Estado actual del proceso de compra."
    )

    proveedor = models.ForeignKey(
        "personas.Proveedor",
        verbose_name="Proveedor",
        on_delete=models.PROTECT,
        related_name="compras",
        help_text="Proveedor al que se realizó la compra."
    )

    movimiento = models.OneToOneField(
        "inventario.Movimiento",
        verbose_name="Movimiento",
        on_delete=models.PROTECT,
        related_name="compra",
        help_text="Movimiento de inventario generado por esta compra."
    )

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = "compra"
        ordering = ["-fecha"]
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return (
            f"{self.proveedor} - "
            f"{self.fecha:%d/%m/%Y %H:%M}"
        )