from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager

class Caja(ModeloBase):

    class Estado(models.TextChoices):
        ABIERTA = "abierta", "Caja abierta"
        CERRADA = "cerrada", "Caja cerrada"

    nombre = models.CharField(
        verbose_name="Nombre de la caja",
        max_length=60,
        help_text="Nombre que identifica la caja dentro del sistema (ej.: Caja Principal, Caja 1, Caja Tienda)."
    )

    descripcion = models.CharField(
        verbose_name="Descripción",
        max_length=255,
        blank=True,
        help_text="Descripción opcional con información adicional sobre la caja."
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=20,
        choices=Estado.choices,
        default=Estado.CERRADA,
        help_text="Estado actual de la caja, indicando si se encuentra habilitada para registrar operaciones de venta."
    )

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = "caja"
        ordering = ["nombre"]
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return self.nombre