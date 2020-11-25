from django.urls import path

from account.views import AccountOverviewView

urlpatterns = [
    path("overview/", AccountOverviewView.as_view(), name="account-overview")
]
