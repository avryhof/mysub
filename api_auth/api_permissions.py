from rest_framework import permissions

from utilities.debugging import log_message
from .models import Application, AppToken


class AuthorizedAppPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        is_authorized = False

        client_id = request.POST.get("client_id")
        client_secret = request.POST.get("client_secret")

        try:
            app = Application.objects.get(client_id=client_id, client_secret=client_secret)
        except Application.DoesNotExist:
            log_message(request.POST, pretty=True)
        else:
            is_authorized = True

        return is_authorized


class AuthorizedTokenPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_authorized = False

        if "Authorization" in request.headers:
            auth = request.headers.get("Authorization")
            token_type, token = auth.split()

            try:
                valid_token = AppToken.objects.get(token_type__iexact=token_type, token=token)
            except AppToken.DoesNotExist:
                pass
            else:
                is_authorized = True

        return is_authorized
