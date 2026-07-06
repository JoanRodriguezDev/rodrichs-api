from django.db import models
from apps.core.models import ModeloBase
from .cliente import Cliente
from .persona_natural import PersonaNatural
from apps.core.managers.active_manager import ActiveManager

class ClienteNatural(ModeloBase):
    
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name="Cliente",
        related_name="cliente_natural", 
        help_text="Cliente base del sistema que actúa como entidad principal para un cliente de tipo natural."
    )
    
    persona_natural = models.OneToOneField(
        PersonaNatural,
        on_delete=models.PROTECT,
        verbose_name="Persona natural",
        related_name="cliente_natural",
        help_text="Datos personales del cliente (nombres, apellidos, documento de identidad, contacto, etc.)."
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "cliente_natural"
        ordering = ["id"]
        verbose_name = "Cliente Natural"
        verbose_name_plural = "Clientes Naturales"
    
    def __str__(self):
        return f"{self.cliente} - {self.persona_natural}"