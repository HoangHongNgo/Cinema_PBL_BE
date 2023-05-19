from rest_framework import generics, filters
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

# Create your views here.


class ListTicketView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Ticket.objects.first()
    serializer_class = TicketSerializer


class ListTicketByCinema(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Ticket.objects.filter()
