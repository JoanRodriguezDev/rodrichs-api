from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from .caja import Caja
from django.utils import timezone

class CajaDetalle(ModeloBase):

    caja = models.ForeignKey(
        Caja,
        verbose_name="Caja",
        on_delete=models.PROTECT,
        related_name="detalles",
        help_text="Caja a la que pertenece la apertura y cierre registrados."
    )

    usuario = models.ForeignKey(
        "usuarios.Usuario",
        verbose_name="Usuario",
        on_delete=models.PROTECT,
        related_name="cajas_detalle",
        help_text="Usuario responsable de la apertura y cierre de la caja."
    )

    fecha_apertura = models.DateTimeField(
        default=timezone.now,
        verbose_name="Fecha de apertura",
        help_text="Fecha y hora en que se realizó la apertura de la caja."
    )

    monto_inicial = models.DecimalField(
        verbose_name="Monto inicial",
        max_digits=12,
        decimal_places=2,
        help_text="Monto de efectivo con el que se inicia la jornada de la caja."
    )

    monto_final = models.DecimalField(
        verbose_name="Monto final",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Monto total de efectivo registrado al momento del cierre de la caja."
    )

    fecha_cierre = models.DateTimeField(
        verbose_name="Fecha de cierre",
        null=True,
        blank=True,
        help_text="Fecha y hora en que se realizó el cierre de la caja."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "caja_detalle"
        ordering = ["-fecha_apertura"]
        verbose_name = "Caja Detalle"
        verbose_name_plural = "Caja Detalles"
    
    def __str__(self):
        return (
            f"{self.caja.nombre} - "
            f"{self.fecha_apertura:%d/%m/%Y %H:%M}"
        )