import json

from django.contrib.sites.models import Site
from django.http import HttpResponse

from html5_boilerplate.utils import generate_manifest, generate_icons, generate_splash_screens
from . import app_settings


def manifest(request):
    generate_icons()
    generate_splash_screens()
    manifest = generate_manifest()

    manifest.update(
        {
            "name": app_settings.PWA_APP_NAME,
            "short_name": app_settings.PWA_APP_NAME,
            "description": app_settings.PWA_APP_DESCRIPTION,
            "start_url": app_settings.PWA_APP_START_URL,
            "display": app_settings.PWA_APP_DISPLAY,
            "scope": app_settings.PWA_APP_SCOPE,
            "orientation": app_settings.PWA_APP_ORIENTATION,
            "background_color": app_settings.PWA_APP_BACKGROUND_COLOR,
            "theme_color": app_settings.PWA_APP_THEME_COLOR,
            "dir": app_settings.PWA_APP_DIR,
            "lang": app_settings.PWA_APP_LANG,
        }
    )

    try:
        site = Site.objects.get_current(request)
    except Site.DoesNotExist:
        pass
    else:
        domain = "%s://%s" % (request.scheme, site.domain)

        if request.scheme not in manifest.get("start_url"):
            manifest["start_url"] = "%s%s" % (domain, manifest.get("start_url"))

        if request.scheme not in manifest.get("scope"):
            manifest["scope"] = "%s%s" % (domain, manifest.get("scope"))

    response = HttpResponse(content_type="application/manifest+json")
    response["Cache-Control"] = "no-cache"

    response.write(json.dumps(manifest))

    return response
