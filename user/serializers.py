from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']




class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'