from django.urls import path

from .views import auth_token_view, token_refresh_view

urlpatterns = [
    path("v1/token/", auth_token_view, name="api-oauth-token"),
    path("v1/token/refresh/", token_refresh_view, name="api-oauth-token-refresh"),
]
