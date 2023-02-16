from rest_framework import serializers
from app_reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        exclude = ['user']





