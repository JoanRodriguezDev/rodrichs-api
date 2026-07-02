from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager

class Categoria(ModeloBase):

    nombre = models.CharField(
        verbose_name='Nombre Categoría',
        max_length=50,
        unique=True,
        help_text='Nombre único que identifica la categoría de los productos dentro del sistema.'
    )

    descripcion = models.CharField(
        verbose_name='Descripción Categoría',
        max_length=255,
        blank=True,
        help_text='Descripción opcional que proporciona información adicional sobre la categoría y su finalidad.'
    )

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = "categoria"
        ordering = ["nombre"]
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f"{self.nombre}"