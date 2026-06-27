from django.db import models
from apps.core.models import ModeloBase
from django.core.validators import RegexValidator

class Permiso(ModeloBase):

    codigo = models.CharField(
        verbose_name='Código Permiso', 
        max_length=100, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-z]+\.[a-z]+$',
                message='El código debe tener el formato modulo.accion en minúsculas (ej: producto.crear).'
            )
        ],
        help_text='Identificador único del permiso utilizado por el sistema (ej: producto.crear, venta.editar).'
    )

    descripcion = models.CharField(
        verbose_name='Descripción Permiso', 
        max_length=255,
        help_text='Describe la acción o funcionalidad que habilita este permiso dentro del sistema.'
    )

    class Meta:
        db_table = "permiso"
        ordering = ["codigo"]
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"