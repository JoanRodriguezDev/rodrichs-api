from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager

class TipoDocumentoIdentidad(ModeloBase):

    codigo = models.CharField(
        verbose_name='Código', 
        max_length=2,
        unique=True, 
        help_text='Código oficial del tipo de documento según SUNAT o catálogo interno (ej: 01 = DNI, 06 = RUC)'
    )

    nombre = models.CharField(
        verbose_name='Documento de Identidad', 
        max_length=50, 
        help_text='Nombre corto del tipo de documento utilizado en operaciones del sistema (clientes, proveedores, etc.)'
    )
    
    descripcion = models.TextField(
        verbose_name='Descripción', 
        blank=True, 
        help_text='Descripción opcional que detalla el uso o alcance del tipo de documento dentro del sistema'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "tipo_documento_identidad"
        ordering = ["codigo"]
        verbose_name = "Tipo de Documento de Identidad"
        verbose_name_plural = "Tipos de Documentos de Identidad"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"