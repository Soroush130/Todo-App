from django.urls import path, include
from rest_framework import routers
from .views import ScoreViewSet

router = routers.DefaultRouter()
router.register(r'scores', ScoreViewSet, basename='scores')

urlpatterns = [
    path('', include(router.urls)),
]