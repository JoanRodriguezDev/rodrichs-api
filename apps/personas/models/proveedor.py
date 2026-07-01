from django.db import models
from apps.core.models import ModeloBase
from apps.core.managers.active_manager import ActiveManager

class Proveedor(ModeloBase):
    class Tipo(models.TextChoices):
        NATURAL = "natural","Natural"
        JURIDICO = "juridico","Juridico"
        VARIOS = "varios","Varios"

    tipo = models.CharField(
        verbose_name='Tipo de proveedor', 
        max_length=10, 
        choices=Tipo.choices, 
        help_text='Define si el proveedor es una persona natural, jurídica o un proveedor genérico (varios). Esto determina qué datos adicionales se deben registrar.'
    )

    objects = ActiveManager()

    all_objects = models.Manager()
    
    class Meta:
        db_table = "proveedor"
        ordering = ["id"]
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    
    def __str__(self):
        return self.get_tipo_display()