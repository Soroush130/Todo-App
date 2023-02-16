from django.urls import path, include
from rest_framework import routers
from .views import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet, basename='reminders')

urlpatterns = [
    path('', include(router.urls)),
]




