from django.db import models
from apps.core.models import ModeloBase
from .tipo_documento_identidad import TipoDocumentoIdentidad
from .pais import Pais
from django.core.validators import RegexValidator
from apps.core.managers.active_manager import ActiveManager

class PersonaNatural(ModeloBase):

    nombres = models.CharField(
        verbose_name='Nombres',
        max_length=100,
        help_text='Nombres registrados en el documento de identidad (DNI, pasaporte u otro).'
    )

    apellido_paterno = models.CharField(
        verbose_name='Apellido Paterno',
        max_length=50,
        help_text='Apellido paterno según documento de identidad oficial.'
    )

    apellido_materno = models.CharField(
        verbose_name='Apellido Materno',
        max_length=50,
        help_text='Apellido materno según documento de identidad oficial.'
    )

    numero_documento = models.CharField(
        verbose_name='Número de Documento',
        max_length=20,
        help_text='Número del documento de identidad según el tipo seleccionado (DNI, CE, pasaporte, etc.).'
    )

    pais = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        verbose_name='País',
        related_name='personas_naturales',
        help_text='País de nacionalidad o procedencia de la persona natural.'
    )

    numero_celular = models.CharField(
        verbose_name='Número de Celular',
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='El número celular solo debe contener dígitos.'
            )
        ],
        blank=True,
        help_text='Número de contacto móvil en formato nacional o internacional sin espacios ni símbolos.'
    )

    email = models.EmailField(
        verbose_name='Correo Electrónico',
        max_length=100,
        blank=True,
        help_text='Correo electrónico válido para notificaciones del sistema (ventas, compras, comprobantes, etc.).'
    )
    
    tipo_documento = models.ForeignKey(
        TipoDocumentoIdentidad,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Documento',
        related_name='personas_naturales',
        help_text='Tipo de documento de identidad asociado a la persona (DNI, CE, pasaporte, etc.).'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "persona_natural"
        ordering = ["apellido_paterno"]
        verbose_name = "Persona Natural"
        verbose_name_plural = "Personas Naturales"
        constraints = [
            models.UniqueConstraint(
                fields=["tipo_documento", "numero_documento"],
                name="unique_doc_por_tipo"
            )
        ]

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"