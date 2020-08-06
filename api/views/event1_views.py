from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.event1 import Event
from ..serializers import EventSerializer, UserSerializer

# Create your views here.
class Events(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes=()
    def get(self, request):
        """Index request"""
        # Return all events, but still require a token by not overriding the permissions classes
        events = Event.objects.all()
        # events = Event.objects.filter(owner=request.user.id)
        data = EventSerializer(events, many=True).data
        return Response(data)

    serializer_class = EventSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        # request.data['event1']['owner'] = request.user.id
        # Serialize/create event1
        event1 = EventSerializer(data=request.data['event1'])
        if event1.is_valid():
            print(event1)
            m = event1.save()
            return Response(event1.data, status=status.HTTP_201_CREATED)
        else:
            return Response(event1.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        event1 = get_object_or_404(Event, pk=pk)
        data = EventSerializer(event1).data
        # Only want to show owned events?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this event')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        event1 = get_object_or_404(Event, pk=pk)
        if not request.user.id == event1.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this event')
        event1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['event1'].get('owner', False):
            del request.data['event1']['owner']

        # Locate Event
        event1 = get_object_or_404(Event, pk=pk)
        if not request.user.id == event1.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this event')

        # Add owner to data object now that we know this user owns the resource
        request.data['event1']['owner'] = request.user.id
        # Validate updates with serializer
        ms = EventSerializer(event1, data=request.data['event1'])
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
