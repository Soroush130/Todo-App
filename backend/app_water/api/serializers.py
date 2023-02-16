from rest_framework.serializers import Serializer
from rest_framework import serializers
# from app_water.models import Water


class WaterSerializer(Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()
