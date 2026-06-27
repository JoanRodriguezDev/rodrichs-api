from django.contrib import admin

from .models import Usuario, Permiso, Empleado, Rol

admin.site.register(Usuario)
admin.site.register(Permiso)
admin.site.register(Rol)
admin.site.register(Empleado)