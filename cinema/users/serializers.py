from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
