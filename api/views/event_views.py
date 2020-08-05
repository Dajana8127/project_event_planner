from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.event import Event
from ..serializers import EventSerializer, UserSerializer

# Create your views here.
class Events(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        # events = Event.objects.all()
        events = Event.objects.filter(owner=request.user.id)
        data = EventSerializer(events, many=True).data
        return Response(data)

    serializer_class = EventSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['event']['owner'] = request.user.id
        # Serialize/create event
        event = EventSerializer(data=request.data['event'])
        if event.is_valid():
            m = event.save()
            return Response(event.data, status=status.HTTP_201_CREATED)
        else:
            return Response(event.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        event = get_object_or_404(Event, pk=pk)
        data = EventSerializer(event).data
        # Only want to show owned events?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this event')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        event = get_object_or_404(Event, pk=pk)
        if not request.user.id == event.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this event')
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['event'].get('owner', False):
            del request.data['event']['owner']

        # Locate Event
        event = get_object_or_404(Event, pk=pk)
        if not request.user.id == event.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this event')

        # Add owner to data object now that we know this user owns the resource
        request.data['event']['owner'] = request.user.id
        # Validate updates with serializer
        ms = EventSerializer(event, data=request.data['event'])
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
