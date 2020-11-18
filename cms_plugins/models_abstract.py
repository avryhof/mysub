from cms.models import CMSPlugin, Title, Page
from django.db import models
from django.urls import reverse, NoReverseMatch

from bootstrap4_extensions.constants import LINK_TARGET_CHOICES


class PluginAbstractLink(CMSPlugin):
    link = models.CharField(max_length=255, blank=True, null=True, help_text="URL Name, Page Slug, or external link")
    title = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True, choices=LINK_TARGET_CHOICES)

    class Meta:
        abstract = True

    def get_short_description(self):
        retn = self.get_link

        if self.title:
            retn = self.title

        return retn

    @property
    def get_link(self):
        retn = "#"

        if self.link:
            if self.link[0] == "/" or self.link.lower()[0:4] == "http":
                retn = self.link
            else:
                try:
                    retn = reverse(self.link)
                except NoReverseMatch:
                    try:
                        cms_page_title = Title.objects.get(slug=self.link, published=True, publisher_is_draft=False)
                        cms_page = Page.objects.get(id=cms_page_title.page_id)
                        retn = cms_page.get_public_url()
                    except (Title.DoesNotExist, Page.DoesNotExist):
                        pass

        return retn


class PluginAbstractFormSubmit(CMSPlugin):
    after_submit_page = models.CharField(
        max_length=255, blank=True, null=True, help_text="URL Name, Page Slug, or external link"
    )

    class Meta:
        abstract = True

    def get_short_description(self):
        retn = self.get_link()

        if self.title:
            retn = self.title

        return retn

    def get_link(self):
        retn = "/"

        if self.after_submit_page:
            if self.after_submit_page[0] == "/" or self.after_submit_page.lower()[0:4] == "http":
                retn = self.after_submit_page
            else:
                try:
                    reverse(self.after_submit_page)
                except NoReverseMatch:
                    try:
                        cms_page_title = Title.objects.get(
                            slug=self.after_submit_page, published=True, publisher_is_draft=False
                        )
                        cms_page = Page.objects.get(id=cms_page_title.page_id)
                        retn = cms_page.get_public_url()
                    except (Title.DoesNotExist, Page.DoesNotExist):
                        pass

        return retn
