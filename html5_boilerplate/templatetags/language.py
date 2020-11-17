from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def language_code(request):
    return getattr(settings, "LANGUAGE_CODE", "")
