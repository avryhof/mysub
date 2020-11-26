from django.forms import Form, URLField, CharField, PasswordInput


class ServerForm(Form):
    url = URLField(required=True, help_text="https://your-server.com:4040")
    username = CharField(required=True)
    password = CharField(required=False, widget=PasswordInput(), help_text="Leave blank if not being changed.")
