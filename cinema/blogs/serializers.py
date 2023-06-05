from rest_framework import serializers
from .models import Blog
from users.serializers import UserNameSerializer
from movies.serializers import MovieNameSerializer
from users.models import User


class BlogDisplaySerializer(serializers.ModelSerializer):
    author = UserNameSerializer()
    movies = MovieNameSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['title', 'summary', 'content', 'author',
                  'created_at', 'updated_at', 'categories', 'images', 'movies']


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Blog
        fields = ['content', 'author']
