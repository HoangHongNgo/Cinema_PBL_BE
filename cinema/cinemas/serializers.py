from rest_framework import serializers
from .models import City, Cinema


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')

    class Meta:
        model = Cinema
        fields = '__all__'
