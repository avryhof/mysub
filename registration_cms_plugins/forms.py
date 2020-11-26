from django_registration.forms import RegistrationForm
from hcaptcha.fields import hCaptchaField


class CaptchaRegistrationForm(RegistrationForm):
    hcaptcha = hCaptchaField()
