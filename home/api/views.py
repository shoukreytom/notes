from rest_framework.generics import (ListAPIView, DestroyAPIView,
                                    RetrieveAPIView, CreateAPIView,
                                    UpdateAPIView)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from account.models import Account
from home.api.serializers import NoteSerializer
from home.models import Note


class NoteListApiView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailApiView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def create_note_api(request):
    account = Account.objects.get(pk=1)
    note = Note(author=account)
    if request.method == 'POST':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_note_api(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'DELETE':
        data = {}
        op = note.delete()
        if op:
            data['success'] = 'Deleted successfully'
        else:
            data['failure'] = 'Failed to delete'
    return Response(data=data)


@api_view(['PUT', ])
def update_note_api(request, pk):
    try:
        note = get_object_or_404(Note, pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'updated successfully'
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)