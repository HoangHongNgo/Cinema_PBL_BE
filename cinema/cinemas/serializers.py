from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')

    class Meta:
        model = Cinema
        fields = '__all__'


class CinemaChainSerializer(serializers.ModelSerializer):
    cinemas = CinemaSerializer(many=True)

    class Meta:
        model = Cinema_Chain
        fields = ['name', 'rating', 'logo_path', 'cinemas']
