from django.db import models
from apps.core.models import ModeloBase
from .permiso import Permiso

class Rol(ModeloBase):

    nombre = models.CharField(
        verbose_name='Nombre Rol', 
        max_length=50, 
        unique=True,
        help_text='Nombre identificador del rol dentro del sistema (ej: administrador, vendedor, cajero).'
    )

    # Relación Many-to-Many con Permiso, para asignar múltiples permisos a un rol
    permisos = models.ManyToManyField(
        Permiso,
        verbose_name='Permisos asignado al rol',
        blank=True,
        related_name="roles",
        help_text='Conjunto de permisos asociados a este rol que determinan las acciones que puede realizar el usuario.'
    )
    class Meta:
        db_table = "rol"
        ordering = ["nombre"]
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        
    def __str__(self):
        return self.nombre