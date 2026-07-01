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
]