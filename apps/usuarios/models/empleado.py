from django.db import models
from apps.core.models import ModeloBase
from django.core.validators import MinValueValidator
from apps.core.managers.active_manager import ActiveManager

class Empleado(ModeloBase):

    class Estado(models.TextChoices):
        ACTIVO = "activo","Activo"
        EN_INDUCCION = "induccion","Inducción"
        EN_PRUEBA = "prueba","Prueba"
        INACTIVO = "inactivo","Inactivo"
        EN_VACACIONES = "vacaciones","Vacaciones"
        LICENCIA_SUELDO = "licencia_sueldo","Licencia goce sueldo"
        LICENCIA_NO_SUELDO = "licencia_no_sueldo","Licencia sin goce sueldo"
        SUSPENDIDO = "suspendido","Suspendido"

    sueldo = models.DecimalField(
        verbose_name='Sueldo',max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        help_text='Remuneración mensual acordada con el empleado, expresada en la moneda configurada para el sistema.'
    )

    estado = models.CharField(
        verbose_name='Estado',
        choices=Estado.choices,
        max_length=30,
        help_text='Estado laboral actual del empleado dentro de la empresa.'
    )

    fecha_contratacion = models.DateTimeField(
        verbose_name='Fecha de contratación',
        help_text='Fecha en la que el empleado inició su relación laboral con la empresa.'
    )

    fecha_termino = models.DateTimeField(
        verbose_name='Fecha de termino',
        help_text='Fecha de finalización de la relación laboral. Déjelo vacío si el empleado continúa laborando.',
        blank=True,
        null=True
    )
    
    direccion = models.CharField(
        verbose_name='Dirección del empleado',
        max_length=255,
        help_text='Dirección de residencia o domicilio actual del empleado.',
        blank=True
    )

    fecha_nacimiento = models.DateField(
        verbose_name='Fecha de nacimiento',
        help_text='Fecha de nacimiento registrada en el documento de identidad del empleado.',
        blank=True,
        null=True
    )

    persona_natural = models.OneToOneField(
        'personas.PersonaNatural',
        verbose_name='Persona',
        on_delete=models.PROTECT,
        related_name='empleado',
        help_text='Persona natural asociada al empleado, que contiene sus datos personales y de identificación.'
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        db_table = "empleado"
        ordering = ["fecha_contratacion"]
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return f"{self.persona_natural} ({self.get_estado_display()})"