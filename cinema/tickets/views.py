from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
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


class BuyTicketsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TicketSerializer(data=data)

        if serializer.is_valid():
            ticket = serializer.save()
            return Response({"ticket_id": ticket.id, "message": "Ticket purchased successfully."})
        else:
            return Response(serializer.errors, status=400)



