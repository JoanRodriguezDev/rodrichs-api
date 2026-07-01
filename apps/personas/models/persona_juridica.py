from django.db import models
from apps.core.models import ModeloBase
from django.core.validators import RegexValidator
from apps.core.managers.active_manager import ActiveManager

class PersonaJuridica(ModeloBase):
    
    class Estado(models.TextChoices):
        ACTIVO = "activo", "Activo"
        SUSPENSION = "suspension", "Suspensión Temporal"
        BAJA_PROVISIONAL = "baja_provisional", "Baja Provisional"
        BAJA_DEFINITIVA = "baja_definitiva", "Baja Definitiva"
        BAJA_PROVISIONAL_OFICIO = "baja_provisional_oficio", "Baja Provisional de Oficio"
        BAJA_DEFINITIVA_OFICIO = "baja_definitiva_oficio", "Baja Definitiva de Oficio"

    class Condicion(models.TextChoices):
        HABIDO = "habido", "Habido"
        NO_HABIDO = "no_habido", "No Habido"

    ruc = models.CharField(
        verbose_name='Número RUC',
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='El número celular solo debe contener dígitos.'
            )
        ],
        help_text='Número de RUC registrado en SUNAT que identifica de forma única a la empresa.'
    )

    razon_social = models.CharField(
        verbose_name='Razón Social',
        max_length=250,
        help_text='Nombre legal de la empresa registrado ante SUNAT.'
    )

    estado = models.CharField(
        verbose_name='Estado de la empresa',
        max_length=40,
        choices=Estado.choices,
        help_text='Estado tributario actual de la empresa según SUNAT (activo, suspendido, baja, etc.).'
    )

    direccion = models.CharField(
        verbose_name='Dirección',
        max_length=250,
        help_text='Dirección fiscal registrada en SUNAT para efectos tributarios.'
    )

    condicion = models.CharField(
        verbose_name='Condición',
        max_length=20,
        choices=Condicion.choices,
        help_text='Condición de la empresa según SUNAT (habido o no habido en el domicilio fiscal).'
    )

    departamento = models.CharField(
        verbose_name='Departamento',
        max_length=50,
        help_text='Departamento del domicilio fiscal registrado en SUNAT.'
    )

    provincia = models.CharField(
        verbose_name='Provincia',
        max_length=50,
        help_text='Provincia del domicilio fiscal registrado en SUNAT.'
    )

    distrito = models.CharField(
        verbose_name='Distrito',
        max_length=50,
        help_text='Distrito del domicilio fiscal registrado en SUNAT.'
    )
    
    ubigeo_sunat = models.CharField(
        verbose_name='Ubigeo SUNAT',
        max_length=10,
        help_text='Código ubigeo oficial utilizado por SUNAT para identificar la ubicación geográfica.'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "persona_juridica"
        ordering = ["razon_social"]
        verbose_name = "Persona Juridica"
        verbose_name_plural = "Personas Juridicas"
    
    def __str__(self):
        return self.razon_social