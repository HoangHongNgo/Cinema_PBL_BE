import base64
from rest_framework import serializers
from .models import Movie


class Base64ImageField(serializers.ImageField):
    def to_representation(self, value):
        if not value:
            return None

        with value.open('rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())

        return encoded_string.decode('utf-8')


class MovieSerializer(serializers.ModelSerializer):
    cover_image = Base64ImageField()
    banner_image = Base64ImageField()

    class Meta:
        model = Movie
        fields = '__all__'
