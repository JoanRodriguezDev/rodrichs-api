from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import ModeloBase
from .rol import Rol
from .empleado import Empleado

class Usuario(AbstractUser, ModeloBase):

    rol = models.ForeignKey(
        Rol,
        verbose_name='Rol',
        on_delete=models.PROTECT,
        related_name='usuarios',
        blank=True,
        null=True,
        help_text='Rol asignado al usuario que define sus permisos dentro del sistema.'
    )

    empleado = models.OneToOneField(
        Empleado,
        verbose_name='Empleado',
        on_delete=models.PROTECT,
        related_name='usuario',
        blank=True,
        null=True,
        help_text='Empleado del sistema asociado a este usuario. Permite vincular la cuenta de acceso con la información laboral.'
    )

    class Meta:
        db_table = "usuario"
        ordering = ["username"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return f"{self.username} - {self.empleado} - {self.rol}"