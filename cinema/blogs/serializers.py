from rest_framework import serializers
from .models import Blog
from users.serializers import UserNameSerializer
from movies.serializers import MovieNameSerializer


class BlogSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()
    movies = MovieNameSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['title', 'summary', 'content', 'author',
                  'created_at', 'updated_at', 'categories', 'images', 'movies']
