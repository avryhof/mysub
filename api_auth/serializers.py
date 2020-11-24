from django.contrib.auth.models import Group, User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)
