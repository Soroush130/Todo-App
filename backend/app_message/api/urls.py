from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]