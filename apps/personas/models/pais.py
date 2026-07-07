from django.db import models
from apps.core.models import ModeloBase
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from apps.core.managers.active_manager import ActiveManager

class Pais(ModeloBase):

    nombre = models.CharField(
        verbose_name="Nombre País",
        max_length=100,
        help_text="Nombre oficial del país."
    )

    iso2 = models.CharField(
        verbose_name="Código ISO 2",
        max_length=2,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{2}$",
                message="Debe contener exactamente 2 letras mayúsculas."
            )
        ],
        help_text="Código ISO de 2 letras del país (ej: PE)."
    )

    iso3 = models.CharField(
        verbose_name="Código ISO 3",
        max_length=3,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{3}$",
                message="Debe contener exactamente 3 letras mayúsculas."
            )
        ],
        help_text="Código ISO de 3 letras del país (ej: PER)."
    )

    codigo_telefonico = models.CharField(
        verbose_name="Código Telefónico",
        max_length=5,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\+\d{1,4}$",
                message="Formato válido: +51, +1, +593"
            )
        ],
        help_text="Código telefónico internacional del país (ej: +51)."
    )
    
    longitud_celular = models.PositiveSmallIntegerField(
        verbose_name="Longitud del número de celular",
        validators=[
            MinValueValidator(4),
            MaxValueValidator(15),
        ],
        help_text="Cantidad de dígitos que debe tener un número de celular en este país."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "pais"
        ordering = ["nombre"]
        verbose_name = "País"
        verbose_name_plural = "Países"
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo_telefonico})"