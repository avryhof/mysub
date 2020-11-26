from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

from account.forms import ServerForm
from subsonic.models import SubsonicServer


class AccountOverviewView(TemplateView):
    name = "Account Overview"
    template_name = "account-overview.html"

    extra_css = []
    extra_javascript = []

    request = None

    def get_context_data(self, **kwargs):
        context = super(AccountOverviewView, self).get_context_data(**kwargs)
        context["page_title"] = self.name
        context["extra_css"] = self.extra_css
        context["extra_javascript"] = self.extra_javascript
        context["request"] = self.request

        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data()

        try:
            server = SubsonicServer.objects.get(user=request.user)
        except SubsonicServer.DoesNotExist:
            server = False

        context["server"] = server

        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountOverviewView, self).dispatch(*args, **kwargs)


class AccountCredentialsView(TemplateView):
    name = "Account Credentials"
    template_name = "account-credentials.html"

    extra_css = []
    extra_javascript = []

    request = None

    def get_context_data(self, **kwargs):
        context = super(AccountCredentialsView, self).get_context_data(**kwargs)
        context["page_title"] = self.name
        context["extra_css"] = self.extra_css
        context["extra_javascript"] = self.extra_javascript
        context["request"] = self.request

        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data()

        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountCredentialsView, self).dispatch(*args, **kwargs)


class EditServerView(TemplateView):
    name = "Edit Server"
    template_name = "edit-server.html"

    extra_css = []
    extra_javascript = []

    request = None

    def get_context_data(self, **kwargs):
        context = super(EditServerView, self).get_context_data(**kwargs)
        context["page_title"] = self.name
        context["extra_css"] = self.extra_css
        context["extra_javascript"] = self.extra_javascript
        context["request"] = self.request

        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data()

        try:
            server = SubsonicServer.objects.get(user=request.user)
        except SubsonicServer.DoesNotExist:
            server = False
            form = ServerForm
        else:
            form = ServerForm(initial=dict(url=server.url, username=server.username))

        context["server"] = server
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data()

        form = ServerForm(request.POST)
        server = False

        if form.is_valid():
            server_url = form.cleaned_data.get("url")
            server_username = form.cleaned_data.get("username")
            server_password = form.cleaned_data.get("password")

            try:
                server = SubsonicServer.objects.get(user=request.user)
            except SubsonicServer.DoesNotExist:
                messages.add_message(request, messages.SUCCESS, "Server Added")
                server = SubsonicServer.objects.create(
                    user=request.user, url=server_url, username=server_username
                )
            else:
                messages.add_message(request, messages.SUCCESS, "Server Updated")
                server.url = server_url
                server.username = server_username
                server.save()

            if server_password:
                server.change_password(server_password)

        context["server"] = server
        context["form"] = form

        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditServerView, self).dispatch(*args, **kwargs)
