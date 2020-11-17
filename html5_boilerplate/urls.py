from django.urls import path

from html5_boilerplate.views import manifest

urlpatterns = [
    path("manifest.json", manifest, name="manifest_json"),
    path("<str:site>.webmanifest", manifest, name="manifest"),
]
