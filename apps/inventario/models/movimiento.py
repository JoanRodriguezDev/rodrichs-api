from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from django.utils import timezone

class Movimiento(ModeloBase):

    class Tipo(models.TextChoices):
        VENTA = "venta", "Venta de productos"
        COMPRA = "compra", "Compra de productos"
        TRASLADO = "traslado", "Traslado entre almacenes"
        AJUSTE = "ajuste", "Ajuste de stock"

    tipo = models.CharField(
        verbose_name="Tipo de movimiento",
        max_length=30,
        choices=Tipo.choices,
        help_text="Tipo de operación que originó el movimiento de inventario, como una venta, compra, traslado o ajuste de stock."
    )

    fecha = models.DateTimeField(
        verbose_name="Fecha del movimiento",
        default=timezone.now,
        help_text="Fecha y hora en que se registró el movimiento en el sistema."
    )

    observacion = models.TextField(
        verbose_name="Observación",
        blank=True,
        help_text="Comentario u observación adicional relacionada con el movimiento, si corresponde."
    )

    usuario = models.ForeignKey(
        "usuarios.Usuario",
        verbose_name="Usuario",
        on_delete=models.PROTECT,
        related_name="movimientos",
        help_text="Usuario responsable de registrar el movimiento en el sistema."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "movimiento"
        ordering = ["-fecha"]
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

    def __str__(self):
        return (
            f"{self.tipo} - "
            f"{self.fecha:%d/%m/%Y %H:%M}"
        )