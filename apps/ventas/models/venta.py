from django.db import models
from django.utils import timezone
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager


class Venta(ModeloBase):

    class Estado(models.TextChoices):
        COMPLETADA = "completada", "Venta completada"
        INCOMPLETA = "incompleta", "Venta incompleta"

    fecha = models.DateTimeField(
        verbose_name="Fecha de la venta",
        default=timezone.now,
        help_text="Fecha y hora en que se registró la venta."
    )

    total = models.DecimalField(
        verbose_name="Total de la venta",
        max_digits=12,
        decimal_places=2,
        help_text="Importe total de la venta, calculado a partir de los productos registrados."
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=20,
        choices=Estado.choices,
        default=Estado.INCOMPLETA,
        help_text="Estado actual del proceso de venta."
    )

    cliente = models.ForeignKey(
        "personas.Cliente",
        verbose_name="Cliente",
        on_delete=models.PROTECT,
        related_name="ventas",
        help_text="Cliente al que se realizó la venta."
    )

    caja = models.ForeignKey(
        "caja.Caja",
        verbose_name="Caja",
        on_delete=models.PROTECT,
        related_name="ventas",
        help_text="Caja desde la cual se registró la venta."
    )

    movimiento = models.OneToOneField(
        "inventario.Movimiento",
        verbose_name="Movimiento",
        on_delete=models.PROTECT,
        related_name="venta",
        help_text="Movimiento de inventario generado por esta venta."
    )

    objects = ActiveManager()
    
    all_objects = models.Manager()

    class Meta:
        db_table = "venta"
        ordering = ["-fecha"]
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return (
            f"Venta #{self.pk} - "
            f"{self.fecha:%d/%m/%Y %H:%M}"
        )