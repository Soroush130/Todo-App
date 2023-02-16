from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app_water.models import Water
from .serializers import WaterSerializer


class WaterViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        works = Water.objects.filter(user=request.user)
        serializer = WaterSerializer(works, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WaterSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            date, count = cd['date'], cd['count']
            try:
                day = Water.objects.get(user=request.user, date=date)
                day.count = count
                day.save()
                return Response({'message': 'Update Day'}, status=status.HTTP_201_CREATED)
            except:
                Water.objects.create(user=request.user, date=date, count=count)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
