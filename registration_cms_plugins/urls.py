from django.urls import path

from registration_cms_plugins.views import log_out_view

urlpatterns = [path("log-out/", log_out_view, name="log-out-view")]
