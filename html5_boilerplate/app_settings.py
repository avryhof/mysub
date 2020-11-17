""" Settings required by django-app. """
from django.conf import settings
import os

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(
    settings,
    "PWA_SERVICE_WORKER_PATH",
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "templates", "serviceworker.js"),
)
# App parameters to include in manifest.json and appropriate meta tags
SITE_NAME = getattr(settings, "SITE_NAME", "MyApp")

THEME_COLOR = getattr(settings, "THEME_COLOR", "#000")
BACKGROUND_COLOR = getattr(settings, "BACKGROUND_COLOR", "#fff")

PWA_APP_DISPLAY = getattr(settings, "PWA_APP_DISPLAY", "standalone")
PWA_APP_SCOPE = getattr(settings, "PWA_APP_SCOPE", "/")
PWA_APP_ORIENTATION = getattr(settings, "PWA_APP_ORIENTATION", "any")
PWA_APP_START_URL = getattr(settings, "PWA_APP_START_URL", "/")
PWA_APP_FETCH_URL = getattr(settings, "PWA_APP_FETCH_URL", "/")

PWA_APP_ICONS = getattr(
    settings,
    "PWA_APP_ICONS",
    [
        {"src": "/static/images/icons/icon-72x72.png", "size": "72x72"},
        {"src": "/static/images/icons/icon-96x96.png", "size": "96x96"},
        {"src": "/static/images/icons/icon-128x128.png", "size": "128x128"},
        {"src": "/static/images/icons/icon-144x144.png", "size": "144x144"},
        {"src": "/static/images/icons/icon-152x152.png", "size": "152x152"},
        {"src": "/static/images/icons/icon-192x192.png", "size": "192x192"},
        {"src": "/static/images/icons/icon-384x384.png", "size": "384x384"},
        {"src": "/static/images/icons/icon-512x512.png", "size": "512x512"},
    ],
)
PWA_APP_SPLASH_SCREEN = getattr(
    settings,
    "PWA_APP_SPLASH_SCREEN",
    [
        {
            "src": "/static/images/icons/splash-640x1136.png",
            "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-750x1334.png",
            "media": "(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-1242x2208.png",
            "media": "(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)",
        },
        {
            "src": "/static/images/icons/splash-1125x2436.png",
            "media": "(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)",
        },
        {
            "src": "/static/images/icons/splash-828x1792.png",
            "media": "(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-1242x2688.png",
            "media": "(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)",
        },
        {
            "src": "/static/images/icons/splash-1536x2048.png",
            "media": "(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-1668x2224.png",
            "media": "(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-1668x2388.png",
            "media": "(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)",
        },
        {
            "src": "/static/images/icons/splash-2048x2732.png",
            "media": "(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)",
        },
    ],
)
PWA_APP_DIR = getattr(settings, "PWA_APP_DIR", "auto")
PWA_APP_LANG = getattr(settings, "PWA_APP_LANG", "en-US")

PWA_ICON_SIZES = [16, 32, 48, 50, 57, 60, 64, 72, 76, 96, 114, 120, 144, 150, 152, 180, 192, 256, 512, 1024]
ICON_SIZES = getattr(settings, "ICON_SIZES", PWA_ICON_SIZES)

DEFAULT_ICON_SRC = os.path.join(settings.BASE_DIR, "html5_boilerplate", "static", "img", "icon.png")
ICON_SRC = getattr(settings, "ICON_SRC", DEFAULT_ICON_SRC)

DEFAULT_SPLASH_SRC = os.path.join(settings.BASE_DIR, "html5_boilerplate", "static", "img", "splash-screen.png")
SPLASH_SRC = getattr(settings, "SPLASH_SRC", DEFAULT_SPLASH_SRC)

DEFAULT_SPLASH_SIZES = [
    (640, 1136),
    (750, 1334),
    (1242, 2208),
    (1125, 2436),
    (828, 1792),
    (1242, 2688),
    (1536, 2048),
    (1668, 2224),
    (1668, 2388),
    (2048, 2732),
    (1334, 750),
    (2208, 1242),
    (640, 960),
    (2048, 1536),
    (768, 1024),
    (1024, 768),
]

SPLASH_SIZES = getattr(settings, "SPLASH_SIZES", DEFAULT_SPLASH_SIZES)

DEFAULT_SPLASH_MEDIA = {
    "640x1136": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    "750x1334": "(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)",
    "1242x2208": "(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)",
    "1125x2436": "(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)",
    "828x1792": "(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)",
    "1242x2688": "(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)",
    "1536x2048": "(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)",
    "1668x2224": "(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)",
    "1668x2388": "(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)",
    "2048x2732": "(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)",
    "1136x640": "(device-width: 568px) and (device-height: 320px) and (-webkit-device-pixel-ratio: 2)",
    "1334x750": "(device-width: 667px) and (device-height: 375px) and (-webkit-device-pixel-ratio: 2)",
    "2208x1242": "(device-width: 1104px) and (device-height: 621px) and (-webkit-device-pixel-ratio: 3)",
    "2436x1125": "(device-width: 812px) and (device-height: 375px) and (-webkit-device-pixel-ratio: 3)",
    "1792x828": "(device-width: 896px) and (device-height: 414px) and (-webkit-device-pixel-ratio: 2)",
    "2688x1242": "(device-width: 896px) and (device-height: 414px) and (-webkit-device-pixel-ratio: 3)",
    "2048x1536": "(device-width: 1024px) and (device-height: 768px) and (-webkit-device-pixel-ratio: 2)",
    "2224x1668": "(device-width: 1112px) and (device-height: 834px) and (-webkit-device-pixel-ratio: 2)",
    "2388x1668": "(device-width: 1194px) and (device-height: 834px) and (-webkit-device-pixel-ratio: 2)",
    "2732x2048": "(device-width: 1366px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)",
}

SPLASH_MEDIA = getattr(settings, "SPLASH_MEDIA", DEFAULT_SPLASH_MEDIA)
