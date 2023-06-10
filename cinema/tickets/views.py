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
                return Response(serializer.data)
            except Payment.DoesNotExist:
                raise NotFound(detail='Payment not found.')

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListPaymentByUser(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PaymentShowSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        queryset = Payment.objects.all()
        owner_id = getattr(self.kwargs, 'owner_id', None)
        if owner_id is not None:
            queryset = queryset.filter(owner=owner_id)
        return queryset
