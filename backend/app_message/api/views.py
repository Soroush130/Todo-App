from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app_message.models import Message
from .serializers import MessageSerializer


class MessageViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        messages = Message.objects.filter(user=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        message = Message.objects.get(pk=pk, user=request.user)
        if message.user == request.user:
            message.delete()
        return Response({'Message': 'Delete Message'}, status=status.HTTP_204_NO_CONTENT)

