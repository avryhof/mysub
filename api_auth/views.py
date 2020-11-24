from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from api_auth.serializers import UserSerializer, GroupSerializer
from cms_plugins.helpers import resolve_link
from utilities.debugging import log_message


def callback_view(request, *args, **kwargs):
    log_message(request.build_absolute_uri())

    return redirect(resolve_link("home"))


class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(RetrieveAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
