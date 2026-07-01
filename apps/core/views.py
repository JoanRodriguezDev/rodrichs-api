from rest_framework import viewsets
from apps.core.utils.eventos_auditoria import registrar_auditoria, modelo_a_auditar_dict
from apps.auditoria.models import Auditoria
class ModeloBaseViewSet(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        instancia = serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

        registrar_auditoria(
            instancia=instancia,
            accion=Auditoria.Accion.CREATE,
            usuario=self.request.user,
            datos_nuevos=modelo_a_auditar_dict(instancia),
        )

    def perform_update(self, serializer):
        instance = self.get_object()
        datos_anteriores = modelo_a_auditar_dict(instance)

        instance = serializer.save(updated_by=self.request.user)

        registrar_auditoria(
            instancia=instance,
            accion=Auditoria.Accion.UPDATE,
            usuario=self.request.user,
            datos_anteriores=datos_anteriores,
            datos_nuevos=modelo_a_auditar_dict(instance),
        )

    def perform_destroy(self, instance):
        datos_anteriores = modelo_a_auditar_dict(instance)
        instance.is_active = False
        instance.updated_by = self.request.user
        instance.save(update_fields=["is_active", "updated_by"])

        registrar_auditoria(
            instancia=instance,
            accion=Auditoria.Accion.SOFT_DELETE,
            usuario=self.request.user,
            data_anterior=datos_anteriores,
        )
    
    def get_permiso_requerido(self):

        base = getattr(
            self,
            "permiso_base",
            self.queryset.model._meta.model_name
        )

        mapa = {
            "list": f"{base}.list",
            "retrieve": f"{base}.view",
            "create": f"{base}.create",
            "update": f"{base}.update",
            "partial_update": f"{base}.update",
            "destroy": f"{base}.delete",
        }

        return mapa.get(self.action)