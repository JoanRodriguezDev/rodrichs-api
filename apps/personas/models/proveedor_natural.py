from django.db import models
from apps.core.models import ModeloBase
from .proveedor import Proveedor
from .persona_natural import PersonaNatural

class ProveedorNatural(ModeloBase):
    
    proveedor = models.OneToOneField(
        Proveedor,
        on_delete=models.PROTECT,
        verbose_name='Proveedor',
        related_name='proveedor_natural',
        help_text='Proveedor base del sistema. Este registro actúa como entidad principal para cualquier proveedor natural.'
    )

    persona_natural = models.OneToOneField(
        PersonaNatural, 
        on_delete=models.PROTECT, 
        verbose_name='Persona natural', 
        related_name='proveedor_natural',
        help_text='Datos personales del proveedor (DNI, nombres, apellidos, etc.) asociados a este proveedor natural.'
    )

    class Meta:
        db_table = "proveedor_natural"
        ordering = ["id"]
        verbose_name = "Proveedor Natural"
        verbose_name_plural = "Proveedores Naturales"
    
    def __str__(self):
        return f"{self.proveedor} - {self.persona_natural}"