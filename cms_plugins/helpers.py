from cms.models import Title, Page
from django.urls import reverse, NoReverseMatch


def resolve_link(link, default="#"):
    retn = default

    if link[0] == "/" or link.lower()[0:4] == "http":
        retn = link
    else:
        try:
            reverse(link)
        except NoReverseMatch:
            try:
                cms_page_title = Title.objects.get(slug=link, published=True, publisher_is_draft=False)
                cms_page = Page.objects.get(id=cms_page_title.page_id)
                retn = cms_page.get_public_url()
            except (Title.DoesNotExist, Page.DoesNotExist):
                pass

    return retn
