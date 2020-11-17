from rest_framework import permissions


class AnonymousPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        is_authorized = True

        return is_authorized
