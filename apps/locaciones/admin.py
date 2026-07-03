from django.contrib import admin
from .models import Sucursal, Almacen, AlmacenDetalleStock

admin.site.register(Sucursal)
admin.site.register(Almacen)
admin.site.register(AlmacenDetalleStock)