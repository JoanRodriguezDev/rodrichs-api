from django.db import models
from apps.core.models import ModeloBase
from .proveedor import Proveedor
from .persona_juridica import PersonaJuridica
from apps.core.managers.active_manager import ActiveManager

class ProveedorJuridico(ModeloBase):

    proveedor = models.OneToOneField(
        Proveedor, 
        on_delete=models.PROTECT, 
        verbose_name='Proveedor',
        related_name='proveedor_juridico', 
        help_text='Proveedor base del sistema. Este registro representa a un proveedor de tipo jurídico dentro de las operaciones de compra.'
    )

    persona_juridica = models.OneToOneField(
        PersonaJuridica, 
        on_delete=models.PROTECT, 
        verbose_name='Persona Jurídica', 
        related_name='proveedor_juridico', 
        help_text='Información legal de la empresa proveedora (RUC, razón social, estado SUNAT, dirección fiscal, etc.).'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "proveedor_juridico"
        ordering = ["id"]
        verbose_name = "Proveedor Jurídico"
        verbose_name_plural = "Proveedores Jurídicos"
    
    def __str__(self):
        return f"{self.proveedor} - {self.persona_juridica}"
