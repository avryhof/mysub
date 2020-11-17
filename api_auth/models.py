import datetime

from django.db.models import Model, BooleanField, CharField, ForeignKey, CASCADE, IntegerField, DateTimeField
from django_extensions.db.fields.json import JSONField
from oauthlib.common import generate_token

from .generators import generate_client_id, generate_client_secret
from .tools import aware_utcnow, make_utc_aware, minutes


class Application(Model):
    enabled = BooleanField(default=True)
    app_name = CharField(max_length=200, blank=True, null=True)
    client_id = CharField(max_length=200, blank=True, null=True)
    client_secret = CharField(max_length=200, blank=True, null=True)
    limit_by_ip = BooleanField(default=False)
    ip_addresses = JSONField(blank=True, null=True)

    def __str__(self):
        retn = self.app_name

        if not self.enabled:
            retn = "[Disabled] %s" % self.app_name

        return retn

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.client_id:
            self.client_id = generate_client_id()

        if not self.client_secret:
            self.client_secret = generate_client_secret()

        super().save(force_insert, force_update, using, update_fields)


class AppToken(Model):
    app = ForeignKey(Application, blank=True, null=True, on_delete=CASCADE)
    token = CharField(max_length=200, blank=True, null=True)
    refresh_token = CharField(max_length=200, blank=True, null=True)
    token_type = CharField(max_length=50, blank=True, null=True, default="Bearer")
    expires_in = IntegerField(null=True, default=minutes(10))
    expires_datetime = DateTimeField(null=True)

    @property
    def expired(self):
        return aware_utcnow() > self.expires_datetime

    def refresh(self):
        new_expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.expires_in)
        self.expires_datetime = make_utc_aware(new_expire)
        self.save()

    def response_dict(self):
        default_dict = dict(
            access_token=self.token,
            refresh_token=self.refresh_token,
            token_type=self.token_type,
            expires_in=self.expires_in,
            expires_datetime=self.expires_datetime.isoformat(),
        )

        if self.refresh_token:
            default_dict.update(refresh_token=self.refresh_token)

        return default_dict

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.token:
            self.token = generate_token()

        if not self.expires_datetime:
            self.expires_datetime = make_utc_aware(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=self.expires_in)
            )
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
