from rest_framework.permissions import BasePermission


class TienePermisoRol(BasePermission):
    """
    RBAC basado en roles con:
    - Superuser bypass
    - Permisos por rol
    - Acceso a propio perfil controlado por permiso específico
    """

    def _tiene_permiso(self, user, permiso):
        """
        Centraliza la lógica de permisos
        """
        return (
            user.rol
            and user.rol.permisos.filter(
                codigo=permiso,
                is_active=True
            ).exists()
        )
    
    def _get_permiso(self, view):
        return getattr(view, "get_permiso_requerido", lambda: None)()
    
    def has_permission(self, request, view):

        user = request.user

        # 🔒 No autenticado
        if not user or not user.is_authenticated:
            return False

        # 🔓 Superusuario bypass total
        if user.is_superuser:
            return True

        # 🔒 Sin rol = sin acceso
        if not user.rol:
            return False

        permiso = self._get_permiso(view)

        # ❗ IMPORTANTE: si no defines permiso, no se asume acceso
        if not permiso:
            return False

        return self._tiene_permiso(user, permiso)

    def has_object_permission(self, request, view, obj):

        user = request.user

        # 🔓 Superusuario bypass total
        if user.is_superuser:
            return True

        permiso = self._get_permiso(view)

        # 🔐 SELF-ACCESS CONTROLADO (perfil usuario)
        if getattr(view, "allow_self_access", False) and obj.id == user.id:
            permisos_self = getattr(view, "permiso_propio", None)
            if permisos_self:
                return self._tiene_permiso(user, permisos_self)
            return request.method in ["GET", "HEAD", "OPTIONS"]

        # 🔒 Sin permiso definido → denegar
        if not permiso:
            return False

        # 🔒 Sin rol → denegar
        if not user.rol:
            return False

        return self._tiene_permiso(user, permiso)