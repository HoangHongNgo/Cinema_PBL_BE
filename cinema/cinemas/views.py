from rest_framework import generics
from .models import City, Cinema
from .serializers import CitySerializer, CinemaSerializer

# Create your views here.


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CinemaList(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
