from rest_framework import serializers
from .models import Blog
from users.serializers import *
from movies.serializers import *


class BlogSerializer(serializers.ModelSerializer):
    author = UserNameSerializer
    movie = MovieNameSerializer

    class Meta:
        model = Blog
        fields = '__all__'
