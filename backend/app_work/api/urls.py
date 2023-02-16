from django.urls import path, include
from .views import WorkViewSet, TypeWorkViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'works', WorkViewSet, basename='works')
router.register(r'type_works', TypeWorkViewSet, basename='works')

urlpatterns = [
    path('', include(router.urls)),
]