from django.contrib import admin

from .models import TipoDocumentoIdentidad, Proveedor, ProveedorNatural, ProveedorJuridico, PersonaNatural, PersonaJuridica, Pais, Cliente, ClienteNatural, ClienteJuridico

admin.site.register(TipoDocumentoIdentidad)
admin.site.register(Proveedor)
admin.site.register(ProveedorNatural)
admin.site.register(ProveedorJuridico)
admin.site.register(PersonaNatural)
admin.site.register(PersonaJuridica)
admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(ClienteNatural)
admin.site.register(ClienteJuridico)