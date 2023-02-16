from rest_framework import serializers
from app_sport.models import Sport, ItemSport


class SportSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sport
        fields = [
            'id',
            'title',
            'members',
            'items'
        ]
