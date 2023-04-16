from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.


class BlogListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
