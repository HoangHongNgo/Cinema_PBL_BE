from rest_framework import serializers
from .models import *


class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = '__all__'
        depth = 2
