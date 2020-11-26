import pprint

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, PasswordResetForm
from django.utils.translation import ugettext_lazy as _
from django_registration.forms import RegistrationForm

from registration_cms_plugins import app_name
from registration_cms_plugins.forms import CaptchaRegistrationForm
from registration_cms_plugins.models import (
    RegistrationFormPluginConfig,
    LoginFormPluginConfig,
    PasswordChangeFormPluginConfig,
    PasswordResetFormPluginConfig,
)


class LoginFormPlugin(CMSPluginBase):
    model = LoginFormPluginConfig
    name = _("Login Form")
    render_template = "login-form-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(LoginFormPlugin, self).render(context, instance, placeholder)
        context.update({"form": AuthenticationForm, "instance": instance})

        return context


plugin_pool.register_plugin(LoginFormPlugin)


class PasswordChangeFormPlugin(CMSPluginBase):
    model = PasswordChangeFormPluginConfig
    name = _("Change Password Form")
    render_template = "password-change-form-plugin.html"
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(PasswordChangeFormPlugin, self).render(context, instance, placeholder)
        request = context.get("request")
        password_change_form = PasswordChangeForm(request.user)
        context.update({"form": password_change_form, "instance": instance})

        return context


plugin_pool.register_plugin(PasswordChangeFormPlugin)


class PasswordResetFormPlugin(CMSPluginBase):
    model = PasswordResetFormPluginConfig
    name = _("Reset Password Form")
    render_template = "password-reset-form-plugin.html"
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(PasswordResetFormPlugin, self).render(context, instance, placeholder)
        context.update({"form": PasswordResetForm, "instance": instance})

        return context


plugin_pool.register_plugin(PasswordResetFormPlugin)


class RegistrationFormPlugin(CMSPluginBase):
    model = RegistrationFormPluginConfig
    name = _("Registration Form")
    render_template = "registration-form-plugin.html"
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(RegistrationFormPlugin, self).render(context, instance, placeholder)
        context.update({"form": CaptchaRegistrationForm, "instance": instance})

        return context


plugin_pool.register_plugin(RegistrationFormPlugin)
