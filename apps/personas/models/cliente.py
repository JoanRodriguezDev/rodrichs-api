from django.db import models
from apps.core.models import ModeloBase


class Cliente(ModeloBase):
    
    class Tipo(models.TextChoices):
        NATURAL = "natural", "Natural"
        JURIDICO = "juridico", "Jurídico"
        VARIOS = "varios", "Varios"

    tipo = models.CharField(
        verbose_name='Tipo de cliente',
        max_length=10,
        choices=Tipo.choices,
        default=Tipo.NATURAL,
        help_text='Define el tipo de cliente registrado en el sistema (natural, jurídico o varios), lo que determina la estructura de datos asociada.'
    )

    class Meta:
        db_table = "cliente"
        ordering = ["id"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.get_tipo_display()