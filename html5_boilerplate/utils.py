import datetime
import logging
import os
import pprint
import re
import sys

from PIL import Image

from html5_boilerplate import app_settings

if os.name == "posix":
    import grp
    import pwd

# from PIL import Image
from django.conf import settings
from django.contrib.sites.models import Site

logger = logging.getLogger(__name__)


def log_message(message, **kwargs):
    pretty = kwargs.get("pretty", False)
    verbosity = kwargs.get("verbosity", False)

    if pretty:
        message = pprint.pformat(message)

    log_message = "%s: %s\n" % (datetime.datetime.now().isoformat()[0:19], message)

    logger.info(message)

    if verbosity:
        sys.stdout.write(log_message)


def chown(path, user, group):
    """
    os.chown() is nice, but this just makes it work more like the commandline.
    :param path:
    :param user:
    :param group:
    :return:
    """
    if os.name == "posix":
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(group).gr_gid
        retn = os.chown(path, uid, gid)
    else:
        retn = True

    return retn


def create_dirs(path, **kwargs):
    echo_status = kwargs.get("echo_status", False)

    was_created = False
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            log_message("Failed to create %s" % path, verbosity=echo_status)
        else:
            # Take control of the path
            chown(path, "www-data", "www-data")
            was_created = True

    return was_created


def url_join(*args):
    os_path = os.path.join(*args)
    path_parts = re.split(r"[/\\]", os_path)

    return "/".join(path_parts)


def generate_icons(**kwargs):
    overwrite = kwargs.get("overwrite", False)
    echo_status = kwargs.get("echo_status", False)

    static_root = getattr(settings, "STATIC_ROOT", False)
    icon_path = os.path.join(static_root, "favicons")

    icon_source = getattr(app_settings, "ICON_SRC", False)
    icon_sizes = getattr(app_settings, "ICON_SIZES", app_settings.PWA_ICON_SIZES)
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]

    if icon_source:
        create_dirs(icon_path, echo_status=echo_status)

        img = Image.open(icon_source)

        ico_target = os.path.join(icon_path, "favicon.ico")
        if overwrite or not os.path.exists(ico_target):
            try:
                img.save(ico_target, sizes=ico_sizes)
            except:
                log_message("Failed to Save %s" % ico_target, verbosity=echo_status)
            else:
                chown(ico_target, "www-data", "www-data")

        icon_sizes = sorted(icon_sizes, reverse=True)
        # Use the same image object, start with the largest size, and work our way down.
        for icon_size in icon_sizes:
            target_file = os.path.join(icon_path, "favicon-%ix%i.png" % (icon_size, icon_size))
            if overwrite or not os.path.exists(target_file):
                img.thumbnail((icon_size, icon_size), Image.ANTIALIAS)
                try:
                    img.save(target_file, "PNG")
                except:
                    log_message("Failed to save %s" % target_file, verbosity=echo_status)
                else:
                    chown(target_file, "www-data", "www-data")
                    log_message("Generated Icon: %s" % target_file)


def generate_manifest(**kwargs):
    static_root = getattr(settings, "STATIC_ROOT", False)
    static_url = getattr(settings, "STATIC_URL", False)

    icon_path = os.path.join(static_root, "favicons")
    icon_url_path = os.path.join(static_url, "favicons")

    target_file = os.path.join(icon_path, "manifest.json")

    icon_sizes = getattr(app_settings, "ICON_SIZES")

    site_name = getattr(app_settings, "SITE_NAME")

    if hasattr(settings, "SITE_ID"):
        current_site = Site.objects.get_current()
        site_name = current_site.name if current_site else getattr(app_settings, "SITE_NAME")

    manifest = {"name": site_name, "icons": []}

    density_factor = 48
    for icon_size in icon_sizes:
        icon_url = url_join(icon_url_path, "favicon-%ix%i.png" % (icon_size, icon_size))

        manifest["icons"].append(
            {
                "src": icon_url,
                "sizes": "%ix%i" % (icon_size, icon_size),
                "type": "image/png",
                # "density": str(round(icon_size / density_factor, 2)),
            }
        )

    splash_sizes = getattr(app_settings, "SPLASH_SIZES")
    for splash_size in splash_sizes:
        splash_url = url_join(icon_url_path, "splash-%ix%i.png" % splash_size)

        manifest["icons"].append(
            {
                "src": splash_url,
                "sizes": "%ix%i" % splash_size,
                "type": "image/png",
                # "density": str(round(icon_size / density_factor, 2)),
            }
        )

    return manifest


def generate_splash_screens(**kwargs):
    overwrite = kwargs.get("overwrite", False)
    echo_status = kwargs.get("echo_status", False)

    static_root = getattr(settings, "STATIC_ROOT", False)
    icon_path = os.path.join(static_root, "favicons")

    splash_source = getattr(app_settings, "SPLASH_SRC", False)
    splash_sizes = getattr(app_settings, "SPLASH_SIZES", [])

    if splash_source:
        create_dirs(icon_path, echo_status=echo_status)

        img = Image.open(splash_source)

        for splash_size in splash_sizes:
            target_file = os.path.join(icon_path, "splash-%ix%i.png" % splash_size)
            if overwrite or not os.path.exists(target_file):
                img.thumbnail(splash_size, Image.ANTIALIAS)
                try:
                    img.save(target_file, "PNG")
                except:
                    log_message("Failed to save %s" % target_file, verbosity=echo_status)
                else:
                    chown(target_file, "www-data", "www-data")
                    log_message("Generated Splash: %s" % target_file)
