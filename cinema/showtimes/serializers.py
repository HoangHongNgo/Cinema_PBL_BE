from rest_framework import serializers
from .models import *


class ShowtimeSerializer(serializers.Serializer):
    class Meta:
        models = Showtime
        fields = ['id', 'start_time']
