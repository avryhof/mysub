from cms.models import CMSPlugin
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, IntegerField, DO_NOTHING, EmailField, BooleanField
from django_extensions.db.fields.json import JSONField
from djangocms_attributes_field.fields import AttributesField
from djangocms_icon.fields import Icon
from filer.fields.image import FilerImageField

from cms_plugins.models_abstract import PluginAbstractLink


class BannerSectionPluginConfig(CMSPlugin):
    text_prefix = CharField(max_length=100, blank=True, null=True)
    rotate_words = JSONField()
    transition_delay = IntegerField(default="2000", validators=[MaxValueValidator(10000), MinValueValidator(0)])
    subheading = CharField(max_length=100, blank=True, null=True)
    background_image = FilerImageField(blank=True, null=True, related_name="bg_image", on_delete=DO_NOTHING)
    attributes = AttributesField()

    def get_short_description(self):
        if self.text_prefix:
            desc = "%s..." % self.text_prefix
        else:
            desc = "Animated Text Banner Section %s" % self.pk

        return desc


class PortfolioItemPluginConfig(PluginAbstractLink):
    image = FilerImageField(blank=True, null=True, related_name="pfi_image", on_delete=DO_NOTHING)
    sub_heading = CharField(max_length=100, blank=True, null=True)
    icon = Icon()

    def get_short_description(self):
        return "%s" % self.title


class SectionHeaderPluginConfig(CMSPlugin):
    heading_prefix = CharField(max_length=100, blank=True, null=True)
    emphasis_word = CharField(max_length=100, blank=True, null=True)
    sub_heading = CharField(max_length=100, blank=True, null=True)

    def get_short_description(self):
        return "%s %s" % (self.heading_prefix, self.emphasis_word)


class TopBarPluginConfig(PluginAbstractLink):
    prompt_text = CharField(max_length=150, blank=True, null=True, default="Have any questions?")
    phone = CharField(max_length=50, blank=True, null=True, default="123-456-7890")
    email = EmailField(blank=True, null=True)
    link_email = BooleanField(default=False, help_text="Best practice is not to link the email address.")
    title = CharField(max_length=255, blank=True, null=True, verbose_name="Login Button Text")
    foreground_color = ColorField(default="#FFFFFF")
    background_color = ColorField(default="#14BDEE")
    login_foreground_color = ColorField(default="#14BDEE")
    login_background_color = ColorField(default="#384158")

    def get_short_description(self):
        return self.prompt_text
