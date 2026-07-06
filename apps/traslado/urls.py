from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.traslado import TrasladoViewSet

router = DefaultRouter()
router.register(r"traslados",TrasladoViewSet,basename="traslados")

urlpatterns = [
    path("",include(router.urls)),
]
