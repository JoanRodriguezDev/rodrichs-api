from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager
from django.core.validators import RegexValidator

class Sucursal(ModeloBase):

    nombre = models.CharField(
        verbose_name="Nombre de la sucursal",
        max_length=60,
        help_text="Nombre con el que se identifica la sucursal dentro del sistema."
    )

    direccion = models.CharField(
        verbose_name="Dirección",
        max_length=255,
        help_text="Dirección física donde se encuentra ubicada la sucursal."
    )

    telefono = models.CharField(
        verbose_name="Teléfono",
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^\d{9}$',
                message='El número de teléfono debe contener exactamente 9 dígitos.'
            )
        ],
        help_text="Número de teléfono de contacto de la sucursal, sin espacios ni caracteres especiales."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "sucursal"
        ordering = ["nombre"]
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.nombre