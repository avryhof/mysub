from django.contrib import admin

from .models import Application, AppToken


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "app_name",
        "enabled",
        "limit_by_ip",
    )
    list_editable = ("enabled",)
    list_filter = ("enabled", "limit_by_ip")


@admin.register(AppToken)
class AppTokenAdmin(admin.ModelAdmin):
    list_display = (
        "app",
        "token",
        "token_type",
        "expires_in",
        "expires_datetime",
    )
    list_filter = ("app", "expires_datetime")
