from rest_framework import serializers
from .models import *


class ShowSerializer(serializers.Serializer):
    class Meta:
        models = Showtime
        fields = '__all__'
