from cms.models import Title, Page
from django import template

from cms_plugins.helpers import resolve_link

register = template.Library()


@register.simple_tag
def cms_url(page_slug):
    retn = "/"

    try:
        cms_page_title = Title.objects.get(slug=page_slug, published=True, publisher_is_draft=False)
    except Title.DoesNotExist:
        pass
    else:
        try:
            cms_page = Page.objects.get(id=cms_page_title.page_id)
        except Page.DoesNotExist:
            pass
        else:
            retn = cms_page.get_public_url()

    return retn


@register.simple_tag
def site_url(page_slug):
    return resolve_link(page_slug)