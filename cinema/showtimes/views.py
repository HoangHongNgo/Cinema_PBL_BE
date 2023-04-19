from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.


class ShowView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Showtime.objects.all()
    serializer_class = ShowSerializer
