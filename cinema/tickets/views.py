from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
# Create your views here.


class ListTicketView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        show_id = self.kwargs['pk']
        queryset = queryset.filter(showtime_id=show_id)
        return queryset


class TicketDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Ticket.objects.first()
    serializer_class = TicketSerializer


class TicketUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def update(self, request, *args, **kwargs):
        ticket = self.get_object()
        owner_id = request.data.get('owner')

        # Retrieve the User instance based on the owner ID
        try:
            owner = get_user_model().objects.get(id=owner_id)
        except get_user_model().DoesNotExist:
            return Response({"error": "Invalid owner ID"})

        serializer = self.get_serializer(
            ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=owner)

        return Response(serializer.data)


class BuyTicketsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TicketSerializer(data=data)

        if serializer.is_valid():
            ticket = serializer.save()
            return Response({"ticket_id": ticket.id, "message": "Ticket purchased successfully."})
        else:
            return Response(serializer.errors, status=400)
