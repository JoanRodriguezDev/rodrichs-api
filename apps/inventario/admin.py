from django.contrib import admin
from .models import Movimiento, MovimientoDetalle, Kardex

admin.site.register(Movimiento)
admin.site.register(MovimientoDetalle)
admin.site.register(Kardex)