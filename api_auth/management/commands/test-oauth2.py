from django.core.management import BaseCommand
from oauth2_provider.models import Application
from requests_oauthlib import OAuth2Session


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

            scope = ["read"]

            oauth = OAuth2Session(client_id, redirect_uri=redirect_url, scope=scope)

            authorization_url, state = oauth.authorization_url("%s/o/authorize/" % oauth_base)

            print("Please go to %s and authorize access." % authorization_url)
            authorization_response = input("Enter the full callback URL")

            token = oauth.fetch_token(
                "%s/o/token/" % oauth_base, authorization_response=authorization_response, verify=False
            )
