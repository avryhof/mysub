import pprint

import requests
from django.core.management import BaseCommand
from oauth2_provider.models import Application


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            oauth_application = Application.objects.get(name="Test Application")
        except Application.DoesNotExist:
            pass
        else:
            oauth_base = "https://127.0.0.1:8000"

            client_id = oauth_application.client_id
            client_secret = oauth_application.client_secret
            redirect_url = oauth_application.redirect_uris.split()[0]

            scope = [
                # "read",
                # "write",
                # "groups"
            ]

            data = {"grant_type": "password", "username": "amosvryhof@proactrx.com", "password": "Activ3Art!"}

            if len(scope) > 0:
                data["scope"] = " ".join(scope)

            response = requests.post(
                "https://127.0.0.1:8000/o/token/", data=data, auth=(client_id, client_secret), verify=False
            )

            access = response.json()

            token_type = access.get("token_type")
            token = access.get("access_token")

            # So, noe we need a bearer token in our headers
            headers = {"Authorization": "{} {}".format(token_type, token)}

            # Retrieve Users
            print("Retrieve Users")
            users_resp = requests.post("https://127.0.0.1:8000/api/users/", headers=headers, verify=False)
            pprint.pprint(users_resp.json())

            print("Retrieve User")
            user_resp = requests.post("https://127.0.0.1:8000/api/users/1/", headers=headers, verify=False)
            pprint.pprint(user_resp.json())

            # Retrieve Groups
            print("Retrieve Groups")
            groups_resp = requests.post("https://127.0.0.1:8000/api/groups/", headers=headers, verify=False)
            pprint.pprint(groups_resp.json())

            # Create User
            # print("Create User")
            # new_user_data = {"username": "foo", "password": "bar"}
            # adduser_resp = requests.post("https://127.0.0.1:8000/api/users/", headers=headers, verify=False)

            # Refresh Token
            # refresh_data = {
            #     "grant_type": "refresh_token",
            #     "refresh_token": access.get("refresh_token"),
            #     "client_id": client_id,
            #     "client_secret": client_secret,
            # }
            # refresh_resp = requests.post("https://127.0.0.1:8000/o/token/", data=refresh_data, verify=False)
            #
            # access = refresh_resp.json()
            #
            # token_type = access.get("token_type")
            # token = access.get("access_token")
