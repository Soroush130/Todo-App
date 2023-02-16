from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app_note.models import Note
from .serializers import NoteSerializer


class NoteViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        note = get_object_or_404(Note.objects.filter(user=request.user), pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def create(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        note = Note.objects.get(pk=pk, user=request.user)
        if note.user == request.user:
            note.delete()
        return Response({'Message': 'Delete Note'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def get_notes_in_day(self, request):
        date = request.data['date'].split('-')
        year, month, day = date[0], date[1], date[2]
        notes_in_day = Note.objects.filter(date__year=year, date__month=month, date__day=day)
        serializer = NoteSerializer(notes_in_day, many=True)
        return Response(serializer.data)
