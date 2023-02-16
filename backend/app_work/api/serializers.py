from rest_framework.serializers import Serializer, ModelSerializer
from app_work.models import Work, TypeWork


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = (
            'id',
            'title',
            'description',
            'time',
            'type_work',
            'is_finished',
            'created'
        )


class TypeWorkSerializer(ModelSerializer):
    class Meta:
        model = TypeWork
        fields = '__all__'
