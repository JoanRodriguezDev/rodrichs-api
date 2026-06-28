from django.contrib.contenttypes.models import ContentType

from apps.auditoria.models import Auditoria


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
    accion,
    request,
    usuario=None,
    objeto=None,
    datos_anteriores=None,
    datos_nuevos=None,
    metadata=None,
):
    """
    Registra un evento de auditoría.

    Parámetros
    ----------
    accion : str
        Acción realizada (CREATE, UPDATE, DELETE, LOGIN, etc.)

    request : HttpRequest
        Request actual para obtener IP y User-Agent.

    usuario : Usuario, opcional
        Usuario que ejecutó la acción.

    objeto : Model, opcional
        Instancia del modelo afectado.

    datos_anteriores : dict, opcional
        Estado del objeto antes de la modificación.

    datos_nuevos : dict, opcional
        Estado del objeto después de la modificación.

    metadata : dict, opcional
        Información adicional.
    """

    nombre_tabla = None
    content_type = None
    object_id = None

    if objeto is not None:
        content_type = ContentType.objects.get_for_model(objeto)

        nombre_tabla = objeto._meta.db_table

        object_id = objeto.pk

    Auditoria.objects.create(
        accion=accion,
        nombre_tabla=nombre_tabla,
        content_type=content_type,
        object_id=object_id,
        datos_anteriores=datos_anteriores,
        datos_nuevos=datos_nuevos,
        usuario=usuario,
        direccion_ip=obtener_direccion_ip(request),
        agente_usuario=request.META.get("HTTP_USER_AGENT"),
        metadata=metadata,
    )