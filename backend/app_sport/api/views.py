from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app_sport.models import Sport, ItemSport
from .serializers import SportSerializer


class SportViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        program_sport = Sport.objects.all()
        serializer = SportSerializer(program_sport, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_program_sport(self, request, pk):
        program_sport = get_object_or_404(Sport.objects.all(), pk=pk)
        program_sport.members.add(request.user)
        return Response({'message': 'add user'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def remove_program_sport(self, request, pk):
        program_sport = get_object_or_404(Sport.objects.all(), pk=pk)
        program_sport.members.remove(request.user)
        return Response({'message': 'remove user'}, status=status.HTTP_200_OK)
