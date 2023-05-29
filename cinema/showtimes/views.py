from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from datetime import datetime

# Create your views here.


class ShowView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ShowtimeSerializer

    def get_queryset(self,  *args, **kwargs):
        queryset = Showtime.objects.all()
        cinema = self.request.query_params.get('cinema')
        date = self.request.query_params.get('date')
        movie = self.request.query_params.get('movie')
        if cinema is not None:
            queryset = queryset.filter(Cinema_Room__cinema=cinema)
        if movie is not None:
            queryset = queryset.filter(movie=movie)
        if date is not None:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            queryset = queryset.filter(start_time__date=date_obj.date())
        return queryset


class ShowDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
