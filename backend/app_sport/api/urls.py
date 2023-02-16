from django.urls import path, include
from rest_framework import routers
from .views import SportViewSet

router = routers.DefaultRouter()
router.register(r'sports', SportViewSet, basename='sports')

urlpatterns = [
    path('', include(router.urls)),
]