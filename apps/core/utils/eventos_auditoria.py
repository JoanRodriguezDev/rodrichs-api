from django.contrib.contenttypes.models import ContentType
from apps.auditoria.models import Auditoria
from datetime import datetime, date, time
from django.db.models.fields.files import FieldFile


def obtener_direccion_ip(request):
    """
    Obtiene la dirección IP real del cliente.
    Compatible con proxies y balanceadores.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()

    return request.META.get("REMOTE_ADDR")

def registrar_auditoria(
    *,
    instancia=None,
    accion,
    usuario=None,
    request=None,
    datos_anteriores=None,
    datos_nuevos=None,
    metadata=None,
):

    ip = obtener_direccion_ip(request) if request else None
    user_agent = getattr(request, "META", {}).get("HTTP_USER_AGENT") if request else None

    Auditoria.objects.create(
        accion=accion,
        nombre_tabla=getattr(instancia, "_meta", None).model_name if instancia else None,
        content_type=ContentType.objects.get_for_model(instancia) if instancia else None,
        object_id=getattr(instancia, "id", None) if instancia else None,
        usuario=usuario,
        datos_anteriores=datos_anteriores,
        datos_nuevos=datos_nuevos,
        direccion_ip=ip,
        agente_usuario=user_agent,
        metadata=metadata,
    )




def modelo_a_auditar_dict(instance):
    data = {}

    for field in instance._meta.fields:
        value = getattr(instance, field.name)

        # ForeignKey
        if field.is_relation:
            data[field.name] = value.id if value else None

        # FileField / ImageField
        elif isinstance(value, FieldFile):
            data[field.name] = value.name if value else None
            # o: value.url si quieres la URL

        # Fechas
        elif isinstance(value, (datetime, date, time)):
            data[field.name] = value.isoformat() if value else None

        # Campos normales
        else:
            data[field.name] = value

    # ManyToMany
    for field in instance._meta.many_to_many:
        data[field.name] = list(
            getattr(instance, field.name).values_list("id", flat=True)
        )

    return data


# Para eventos de Login, Login fallido, Logout.
def registrar_evento(
    *,
    accion,
    usuario=None,
    request=None,
    metadata=None,
):
    Auditoria.objects.create(
        accion=accion,
        usuario=usuario,
        direccion_ip=obtener_direccion_ip(request) if request else None,
        agente_usuario=getattr(request, "META", {}).get("HTTP_USER_AGENT") if request else None,
        metadata=metadata,
    )