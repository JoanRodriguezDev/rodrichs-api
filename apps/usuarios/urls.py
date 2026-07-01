from django.urls import path
from apps.usuarios.views.auth import (
    LoginView,
    MeView,
    RefreshView,
    LogoutView,
)


urlpatterns = [
    path(
        "usuarios/auth/login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "usuarios/auth/me/",
        MeView.as_view(),
        name="me",
    ),

    path(
        "usuarios/auth/refresh/",
        RefreshView.as_view(),
        name="refresh",
    ),

    path(
        "usuarios/auth/logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]

#Endpoints disponibles:
# /api/v1/usuarios/auth/me/ -> Devuelve la información del usuario autenticado
# /api/v1/usuarios/auth/login/ -> Permite iniciar sesión y obtener tokens JWT
# /api/v1/usuarios/auth/refresh/ -> Permite refrescar el token de acceso utilizando el token de refresco
# /api/v1/usuarios/auth/logout/ -> Permite cerrar sesión y revocar el token de refresco