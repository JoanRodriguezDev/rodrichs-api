from django.urls import include, path

urlpatterns = [
    path(
        "",
        include("apps.usuarios.urls")
    ),
    path(
        "",
        include("apps.personas.urls")
    ),
    path(
        "",
        include("apps.catalogo.urls")
    ),
    path(
        "",
        include("apps.caja.urls")
    ),
    path(
        "",
        include("apps.locaciones.urls")
    ),
    path(
        "",
        include("apps.inventario.urls")
    ),
]