from .models import AppToken
from .responses import (
    INVALID_GRANT_RESPONSE,
    UNSUPPORTED_GRANT_TYPE_RESPONSE,
    INVALID_CLIENT_RESPONSE,
    INVALID_REQUEST_RESPONSE,
)


def clean_expired_tokens():
    for tk in AppToken.objects.all():
        if tk.expired:
            tk.delete()


def get_ip_address(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def check_ip_address(request, app):
    retn = True

    if app.limit_by_ip:
        ip = get_ip_address(request)

        if ip not in list(app.ip_addresses):
            retn = INVALID_CLIENT_RESPONSE

    return retn


def check_token(request, **kwargs):
    check_expired = kwargs.get("check_expired", True)

    auth = request.headers.get("Authorization", False)

    if not auth:
        token = INVALID_REQUEST_RESPONSE
    else:
        token_type, token = auth.split()

        try:
            token = AppToken.objects.get(token=token)
        except AppToken.DoesNotExist:
            token = INVALID_GRANT_RESPONSE
        else:
            if token_type != token.token_type:
                token = UNSUPPORTED_GRANT_TYPE_RESPONSE
            else:
                token = token

            if check_expired and token.expired:
                token = INVALID_GRANT_RESPONSE

            if hasattr(token, "app"):
                ip_status = check_ip_address(request, token.app)
                if ip_status != True:  # Do not "simplify this, it returns either True or a Response object)
                    token = ip_status

    return token
