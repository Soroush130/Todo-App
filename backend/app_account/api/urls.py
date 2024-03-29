from django.urls import path, include
from rest_framework import routers
from .views import RegisterViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]
