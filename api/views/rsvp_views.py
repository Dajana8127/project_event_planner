# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

from ..serializers import RSVPSerializer
from ..models.rsvp import RSVP

class RSVPs(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = RSVPSerializer
    def post(self, request):
        """Create request"""
        # get_queryset(self, request)
        print(request.data)
        request.data['rsvp']['owner'] = request.user.id
        rsvp = RSVPSerializer(data=request.data['rsvp'])
        if rsvp.is_valid():
            rsvp.save()
            return Response(rsvp.data, status=status.HTTP_201_CREATED)
        else:
            return Response(rsvp.errors, status=status.HTTP_400_BAD_REQUEST)

class RSVPDetail(generics.DestroyAPIView):
    # permission_classes=(IsAuthenticated,)
    # serializer_class = RSVPSerializer
    # def patch(self, requests, pk):
    #     """Update Request"""
    #     rsvp = get_object_or_404(RSVP, pk=pk)
    #     ms = RSVPSerializer(rsvp, data=request.data['rsvp'], patial=True)
    #     if request.data['rsvp'].get('owner', False):
    #         del request.data['rsvp']['owner']
    #
    #     rsvp = get_object_or_404(RSVP, pk=pk)
    #     if not request.user.id == rsvp.owner.id:
    #         raise PermissionDenied('Unauthorized')
    #
    #     request.data['rsvp']['owner'] = request.user.id
    #     new_rsvp = RSVPSerializer(rsvp, data=request.data['rsvp'])
    #     if new_rsvp.is_valid():
    #         new_rsvp.save()
    #         return Response(new_rsvp.data)
    #     else:
    #         return Response(new_rsvp.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        rsvp = get_object_or_404(RSVP, pk=pk)
        if not request.user.id == rsvp.owner.id:
            raise PermissionDenied('Unauthorized')
        else:
            rsvp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
