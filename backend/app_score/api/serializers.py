from rest_framework import serializers
from app_score.models import Score


class ScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    month = serializers.DateField()
    score = serializers.IntegerField()
