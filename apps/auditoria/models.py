from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

class Auditoria(models.Model):
    
    class Accion(models.TextChoices):
        CREATE = "CREATE", "Crear"
        UPDATE = "UPDATE", "Actualizar"
        DELETE = "DELETE", "Eliminar"
        SOFT_DELETE = "SOFT_DELETE", "Eliminación lógica"
        LOGIN = "LOGIN", "Inicio de sesión"
        LOGOUT = "LOGOUT", "Cierre de sesión"
        LOGIN_FAILED = "LOGIN_FAILED", "Intento de inicio fallido"

    accion = models.CharField(
        verbose_name="Acción",
        max_length=50,
        choices=Accion.choices,
        help_text="Acción realizada sobre el registro."
    )

    nombre_tabla = models.CharField(
        verbose_name="Nombre de la tabla",
        max_length=100,
        null=True,
        blank=True,
        help_text="Nombre de la tabla o modelo afectado por la acción."
    )

    object_id = models.PositiveIntegerField(
        verbose_name="ID del objeto",
        null=True,
        blank=True,
        help_text="Identificador del registro afectado."
    )

    content_type = models.ForeignKey(
        ContentType,
        verbose_name="Tipo de contenido",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Modelo al que pertenece el registro auditado."
    )

    datos_anteriores = models.JSONField(
        verbose_name="Datos anteriores",
        null=True,
        blank=True,
        help_text="Estado del registro antes de realizar la acción."
    )

    datos_nuevos = models.JSONField(
        verbose_name="Datos nuevos",
        null=True,
        blank=True,
        help_text="Estado del registro después de realizar la acción."
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuario",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Usuario que ejecutó la acción."
    )

    direccion_ip = models.GenericIPAddressField(
        verbose_name="Dirección IP",
        null=True,
        blank=True,
        help_text="Dirección IP desde la que se realizó la solicitud."
    )

    agente_usuario = models.TextField(
        verbose_name="Agente de usuario",
        null=True,
        blank=True,
        help_text="Información del navegador o cliente que realizó la solicitud."
    )

    metadata = models.JSONField(
        verbose_name="Metadatos",
        null=True,
        blank=True,
        help_text="Información adicional relacionada con el evento de auditoría."
    )

    fecha = models.DateTimeField(
        verbose_name="Fecha",
        auto_now_add=True,
        help_text="Fecha y hora en que ocurrió la acción."
    )

    class Meta:
        db_table = "auditoria"
        ordering = ["-fecha", "-id"] # Muestra por menor fecha y id
        verbose_name = "Auditoria"
        verbose_name_plural = "Auditorias"

    def __str__(self):
        return f"{self.accion} - {self.nombre_tabla or 'Login'} ({self.fecha:%d/%m/%Y %H:%M})"
