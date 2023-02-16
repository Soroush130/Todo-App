from rest_framework import serializers
from app_message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['user']
