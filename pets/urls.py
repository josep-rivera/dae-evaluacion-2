from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r"entidad1", PetViewSet, basename="pet")
router.register(r"entidad2", OwnerViewSet, basename="owner")

urlpatterns = [
    path("", include(router.urls)),
]
