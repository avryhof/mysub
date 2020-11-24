from django.urls import path

from api_auth.views import UserList, UserDetails, GroupList

urlpatterns = [
    path("users/", UserList.as_view(), name="api-users"),
    path("users/<pk>/", UserDetails.as_view(), name="api-user"),
    path("groups/", GroupList.as_view(), name="api-groups"),
]
