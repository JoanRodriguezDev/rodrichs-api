from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Usuario, Permiso, Empleado, Rol

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.all()

admin.site.register(Permiso)
admin.site.register(Rol)
admin.site.register(Empleado)