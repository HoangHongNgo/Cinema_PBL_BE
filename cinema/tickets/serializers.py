from rest_framework import serializers
from .models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'showtime', 'seat_num',
                  'seat_row', 'sale_date', 'price', 'owner']
        depth = 2
