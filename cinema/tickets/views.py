from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound, MethodNotAllowed
# Create your views here.


class ListTicketView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        show_id = getattr(self.kwargs, 'pk', None)
        if show_id is not None:
            queryset = queryset.filter(showtime_id=show_id)
        return queryset


class CreateOrUpdatePayment(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateOrUpdatePaymentSerializer

    def patch(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def put(self, request, *args, **kwargs):
        payment_id = request.data.get('id')

        if payment_id:
            try:
                payment = Payment.objects.get(id=payment_id)
                serializer = self.serializer_class(payment, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                tickets_id = serializer.data.get('tickets')
                tickets = Ticket.objects.filter(id__in=tickets_id)
                ticket_data = TicketSerializer(tickets, many=True).data

                for ticket in ticket_data:
                    del ticket['payment']

                response_data = {
                    'id': serializer.data.get('id'),
                    'owner': serializer.data.get('owner'),
                    'tickets': ticket_data
                }

                return Response(response_data)
            except Payment.DoesNotExist:
                raise NotFound(detail='Payment not found.')

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tickets_id = serializer.data.get('tickets')
        tickets = Ticket.objects.filter(id__in=tickets_id)
        ticket_data = TicketSerializer(tickets, many=True).data

        for ticket in ticket_data:
            del ticket['payment']

        response_data = {
            'id': serializer.data.get('id'),
            'owner': serializer.data.get('owner'),
            'tickets': ticket_data
        }

        return Response(response_data)


class ListPaymentByUser(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PaymentShowSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        queryset = Payment.objects.all()
        owner_id = self.kwargs.get('owner')
        if owner_id is not None:
            queryset = queryset.filter(owner=owner_id)
            return queryset
        return None
