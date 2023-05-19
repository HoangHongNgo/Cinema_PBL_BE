from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.


class ShowView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ShowtimeSerializer

    def get_queryset(self,  *args, **kwargs):
        queryset = Showtime.objects.all()
        cinema = self.request.query_params.get('cinema')
        movie = self.request.query_params.get('movie')
        if cinema is not None:
            queryset = queryset.filter(Cinema_Room__cinema=cinema)
        if movie is not None:
            queryset = queryset.filter(movie=movie)
        return queryset
