from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app_score.models import Score
from .serializers import ScoreSerializer


class ScoreViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        list_month = Score.objects.filter(user=request.user)
        serializer = ScoreSerializer(list_month, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        month = get_object_or_404(Score.objects.all(), pk=pk)
        serializer = ScoreSerializer(month)
        return Response(serializer.data)

    def create(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            month, score = cd['month'], cd['score']
            try:
                date = Score.objects.get(user=request.user, month=month)
                date.score = score
                date.save()
                return Response({'message': f'Update Month {month} and score {score}'}, status=status.HTTP_201_CREATED)
            except:
                Score.objects.create(user=request.user, month=month, score=score)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk):
    #     month = get_object_or_404(Score.objects.all(), pk=pk)
    #     serializer = ScoreSerializer(month, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
