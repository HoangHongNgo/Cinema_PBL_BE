from rest_framework import generics, filters
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

# Create your views here.


class CityList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CinemaList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CinemaChainSerializer

    def get_queryset(self):
        queryset = Cinema_Chain.objects.order_by("rating")
        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(city__id=city)
        return queryset


class CinemaByCity(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CinemaChainSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city')
        queryset = Cinema_Chain.objects.order_by(
            "rating")
        if city is not None:
            queryset = queryset.filter(cinema__city__id=city)
        return queryset


class CinemaDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Cinema_Chain.objects.all()
    serializer_class = CinemaSerializer
