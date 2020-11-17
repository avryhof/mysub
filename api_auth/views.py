from oauthlib.oauth2.rfc6749.tokens import random_token_generator
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .api_permissions import AuthorizedAppPermission, AuthorizedTokenPermission
from .helpers import clean_expired_tokens, check_token, check_ip_address
from .models import Application, AppToken
from .responses import INVALID_CLIENT_RESPONSE, SuccessResponse, INVALID_REQUEST_RESPONSE


@api_view(["POST"])
@permission_classes((AuthorizedAppPermission,))
@authentication_classes(())
def auth_token_view(request):
    client_id = request.POST.get("client_id")
    client_secret = request.POST.get("client_secret")

    if not client_id or not client_secret:
        resp = INVALID_REQUEST_RESPONSE
    else:
        clean_expired_tokens()

        try:
            app = Application.objects.get(client_id=client_id, client_secret=client_secret)
        except Application.DoesNotExist:
            resp = INVALID_CLIENT_RESPONSE

        else:
            ip_status = check_ip_address(request, app)
            if ip_status != True:
                resp = ip_status
            else:
                app_token = AppToken.objects.create(app=app, token=random_token_generator(request))

                resp = SuccessResponse(app_token.response_dict())

    return resp


@api_view(["POST"])
@permission_classes((AuthorizedTokenPermission,))
@authentication_classes(())
def token_refresh_view(request):
    auth = request.headers.get("Authorization", False)

    if not auth:
        resp = INVALID_REQUEST_RESPONSE
    else:
        clean_expired_tokens()
        token = check_token(request, check_expired=False)

        if not hasattr(token, "token"):
            return token
        else:
            token.refresh()
            resp = SuccessResponse(token.response_dict())

    return resp
