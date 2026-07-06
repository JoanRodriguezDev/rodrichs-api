from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import ModeloMarcaTiempo
from .rol import Rol
from .empleado import Empleado
from django.contrib.auth.models import UserManager
from apps.core.managers.active_user_manager import ActiveUserManager

class Usuario(AbstractUser, ModeloMarcaTiempo):

    rol = models.ForeignKey(
        Rol,
        verbose_name="Rol",
        on_delete=models.PROTECT,
        related_name="usuarios",
        blank=True,
        null=True,
        help_text="Rol asignado al usuario que define sus permisos dentro del sistema."
    )

    empleado = models.OneToOneField(
        Empleado,
        verbose_name="Empleado",
        on_delete=models.PROTECT,
        related_name="usuario",
        blank=True,
        null=True,
        help_text="Empleado del sistema asociado a este usuario. Permite vincular la cuenta de acceso con la información laboral."
    )

    objects = ActiveUserManager()

    all_objects = UserManager()

    class Meta:
        db_table = "usuario"
        ordering = ["username"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return f"{self.username} - {self.empleado} - {self.rol}"