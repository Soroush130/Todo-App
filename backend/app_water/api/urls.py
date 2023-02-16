from django.urls import path, include
from rest_framework import routers
from .views import WaterViewSet

router = routers.DefaultRouter()
router.register(r'waters', WaterViewSet, basename='works')

urlpatterns = [
    path('', include(router.urls)),
]