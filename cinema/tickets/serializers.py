from rest_framework import serializers
from .models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        depth = 2

class PaymentCreateSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer
    class Meta:
        model = Payment
        fields = ['owner', 'tickets']

class PaymentShowSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer
    class Meta:
        model = Payment
        fields = ['tickets']
        depth = 2