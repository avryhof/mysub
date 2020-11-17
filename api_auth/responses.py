from rest_framework import status
from rest_framework.response import Response

from api_auth.constants import NO_CACHE_HEADERS

ERROR_KEY = "error"
ERROR_DESCRIPTION_KEY = "error_description"
ERROR_URI_KEY = "error_uri"

INVALID_REQUEST_MESSAGE = "invalid_request"
INVALID_CLIENT_MESSAGE = "invalid_client"
INVALID_GRANT_MESSAGE = "invalid_grant"
INVALID_SCOPE_MESSAGE = "invalid_scope"
UNAUTHORIZED_CLIENT_MESSAGE = "unauthorized_client"
UNSUPPORTED_GRANT_TYPE_MESSAGE = "unsupported_grant_type"

INVALID_CLIENT_RESPONSE = Response(
    {ERROR_KEY: INVALID_CLIENT_MESSAGE}, status=status.HTTP_401_UNAUTHORIZED, headers=NO_CACHE_HEADERS
)

INVALID_REQUEST_RESPONSE = Response(
    {ERROR_KEY: INVALID_REQUEST_MESSAGE}, status=status.HTTP_400_BAD_REQUEST, headers=NO_CACHE_HEADERS,
)

INVALID_GRANT_RESPONSE = Response(
    {ERROR_KEY: INVALID_GRANT_MESSAGE, ERROR_DESCRIPTION_KEY: "The access_token is invalid or expired."},
    status=status.HTTP_401_UNAUTHORIZED,
    headers=NO_CACHE_HEADERS,
)

UNAUTHORIZED_CLIENT_RESPONSE = Response(
    {ERROR_KEY: UNAUTHORIZED_CLIENT_MESSAGE}, status=status.HTTP_401_UNAUTHORIZED, headers=NO_CACHE_HEADERS
)

UNSUPPORTED_GRANT_TYPE_RESPONSE = Response(
    {ERROR_KEY: UNSUPPORTED_GRANT_TYPE_MESSAGE}, status=status.HTTP_400_BAD_REQUEST, headers=NO_CACHE_HEADERS,
)


def SuccessResponse(data):
    return Response(data, status=status.HTTP_200_OK, headers=NO_CACHE_HEADERS)
