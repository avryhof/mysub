from django.conf import settings
from django.contrib.sites.models import Site

from utilities.custom_site_class import CustomSite


def website_context(request):
    site_name = ""

    site = CustomSite(request)

    try:
        current_site = Site.objects.get_current(request)
    except Site.DoesNotExist:
        if settings.SITE_ID:
            current_site = Site.objects.get(pk=settings.SITE_ID)
            return_dict = {
                "site_url": site.site_url,
                "domain_name": site.domain,
                "site_name": current_site.name,
            }
        else:
            return_dict = {
                "site_url": site.site_url,
                "domain_name": site.domain,
                "site_name": site_name,
            }

    else:
        return_dict = {
            "site_url": site.site_url,
            "domain_name": site.domain,
            "site_name": current_site.name,
        }

    return return_dict
