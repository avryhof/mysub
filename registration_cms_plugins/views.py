from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme

from cms_plugins.helpers import resolve_link


def log_out_view(request, *args, **kwargs):
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME

    auth_logout(request)

    if next_page is not None:
        next_page = resolve_link(next_page)
    elif settings.LOGOUT_REDIRECT_URL:
        next_page = resolve_link(settings.LOGOUT_REDIRECT_URL)
    else:
        next_page = next_page

    if redirect_field_name in request.POST or redirect_field_name in request.GET:
        next_page = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name))
        url_is_safe = url_has_allowed_host_and_scheme(url=next_page, require_https=request.is_secure(),)
        # Security check -- Ensure the user-originating redirection URL is safe.
        if not url_is_safe:
            next_page = request.path

    return HttpResponseRedirect(next_page)
