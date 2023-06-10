from rest_framework import serializers
from .models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        depth = 2


class CreateOrUpdatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'owner', 'tickets')

    def create(self, validated_data):
        tickets_id = validated_data.pop('tickets')
        payment = Payment.objects.create(**validated_data)
        payment.tickets.set(tickets_id)

        return payment

    def update(self, instance, validated_data):
        tickets_id = validated_data.pop('tickets')

        instance.id = validated_data.get('id', instance.id)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        instance.tickets.set(tickets_id)

        return instance


class PaymentShowSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer

    class Meta:
        model = Payment
        fields = ['id', 'tickets']
        depth = 2
