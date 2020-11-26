from django.urls import path

from account.views import AccountOverviewView, EditServerView, AccountCredentialsView

urlpatterns = [
    path("overview/", AccountOverviewView.as_view(), name="account-overview"),
    path("credentials/", AccountCredentialsView.as_view(), name="account-credentials"),
    path("edit-server/", EditServerView.as_view(), name="edit-server"),
]
