from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.


class BlogView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogDisplaySerializer


class BlogAddView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
