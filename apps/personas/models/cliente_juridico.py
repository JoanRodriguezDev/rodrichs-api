from django.db import models
from apps.core.models import ModeloBase
from .cliente import Cliente
from .persona_juridica import PersonaJuridica
from apps.core.managers.active_manager import ActiveManager

class ClienteJuridico(ModeloBase):

    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name='Cliente',
        related_name='cliente_juridico',
        help_text='Cliente base del sistema que actúa como entidad principal para un cliente de tipo jurídico.'
    )
    
    persona_juridica = models.OneToOneField(
        PersonaJuridica,
        on_delete=models.PROTECT,
        verbose_name='Persona jurídica',
        related_name='cliente_juridico',
        help_text='Información legal de la empresa cliente (RUC, razón social, estado SUNAT, dirección fiscal, etc.).'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "cliente_juridico"
        ordering = ["id"]
        verbose_name = "Cliente Jurídico"
        verbose_name_plural = "Clientes Jurídicos"
    
    def __str__(self):
        return f"{self.cliente} - {self.persona_juridica}"