import base64
from rest_framework import serializers
from .models import Movie


# class Base64ImageField(serializers.ImageField):
#     def to_representation(self, value):
#         if not value:
#             return None

#         with value.open('rb') as image_file:
#             encoded_string = base64.b64encode(image_file.read())

#         return encoded_string.decode('utf-8')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class MovieNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name']


class MovieTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['trailer_id']


class MovieCoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['cover_image']


class MovieBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['banner_image']
