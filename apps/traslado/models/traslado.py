from django.db import models
from django.utils import timezone
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager


class Traslado(ModeloBase):

    class Estado(models.TextChoices):
        COMPLETADO = "completado", "Completado"
        INCOMPLETO = "incompleto", "Incompleto"

    fecha = models.DateTimeField(
        verbose_name="Fecha del traslado",
        default=timezone.now,
        help_text="Fecha y hora en que se registró el traslado entre almacenes."
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=20,
        choices=Estado.choices,
        default=Estado.INCOMPLETO,
        help_text="Estado actual del proceso de traslado."
    )

    movimiento = models.OneToOneField(
        "inventario.Movimiento",
        verbose_name="Movimiento",
        on_delete=models.PROTECT,
        related_name="traslado",
        help_text="Movimiento de inventario asociado a este traslado."
    )

    almacen_origen = models.ForeignKey(
        "locaciones.Almacen",
        verbose_name="Almacén de origen",
        on_delete=models.PROTECT,
        related_name="traslados_salida",
        help_text="Almacén desde el cual se envían los productos."
    )

    almacen_destino = models.ForeignKey(
        "locaciones.Almacen",
        verbose_name="Almacén de destino",
        on_delete=models.PROTECT,
        related_name="traslados_entrada",
        help_text="Almacén al que se trasladan los productos."
    )

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = "traslado"
        ordering = ["-fecha"]
        verbose_name = "Traslado"
        verbose_name_plural = "Traslados"

    def __str__(self):
        return (
            f"{self.almacen_origen} → "
            f"{self.almacen_destino} "
            f"({self.fecha:%d/%m/%Y %H:%M})"
        )