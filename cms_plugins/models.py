from cms.models import CMSPlugin, Title, Page
from django.db import models
from django.db.models import DO_NOTHING
from djangocms_attributes_field.fields import AttributesField
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

from cms_plugins.constants import (
    BLOCK_TAGS,
    TEXT_CLASSES,
    BACKGROUND_CLASSES,
    BACKGROUND_SIZE_COVER,
    BACKGROUND_SIZE_CHOICES,
    HEADING_TYPES, AUTH_USER_CHOICES, AUTHENTICATED_USERS,
)
from cms_plugins.models_abstract import PluginAbstractLink


class AuthenticatedUserPluginConfig(CMSPlugin):
    show_to = models.CharField(max_length=100, choices=AUTH_USER_CHOICES, default=AUTHENTICATED_USERS)
    unauthenticated_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Authenticated User Content"

    def get_short_description(self):
        return "Content for Authenticated User"


class BlockTagPluginConfig(CMSPlugin):
    tag_type = models.CharField(max_length=50, choices=BLOCK_TAGS, blank=True, null=True)
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    show_background_image = models.BooleanField(default=False)
    background_image = FilerImageField(blank=True, null=True, related_name="bt_bg_image", on_delete=DO_NOTHING)

    background_size_class = models.CharField(
        max_length=30, default=BACKGROUND_SIZE_COVER, choices=BACKGROUND_SIZE_CHOICES
    )
    attributes = AttributesField(excluded_keys=("class", "style",))

    @property
    def class_str(self):
        class_list = []

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)


class DIVPluginConfig(CMSPlugin):
    title = models.CharField(max_length=200, blank=True, null=True)
    attributes = AttributesField()

    def __str__(self):
        return "Div Plugin %s" % str(self.pk)

    def get_short_description(self):
        return "Div Plugin %s" % str(self.title)


class ExpanderPluginConfig(CMSPlugin):
    text = models.CharField(max_length=255, blank=True, null=True)
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    attributes = AttributesField()

    @property
    def slug(self):
        return "expander-%s" % self.pk

    @property
    def class_str(self):
        class_list = []

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)

    def __str__(self):
        return "Expander: %s" % self.text

    def get_short_description(self):
        return "Expander: %s" % self.text


class HeadingPluginConfig(CMSPlugin):
    text = models.CharField(max_length=255, blank=True, null=True)
    tag_type = models.CharField(max_length=50, choices=HEADING_TYPES, blank=True, null=True)
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    attributes = AttributesField()

    @property
    def class_str(self):
        class_list = []

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)

    def __str__(self):
        return "Heading: %s" % str(self.pk)

    def get_short_description(self):
        retn = "Heading: %s" % str(self.pk)

        if self.text:
            retn = self.text

        return retn


class List(CMSPlugin):
    LIST_BLANK_CHOICE = ("None", None)

    ORDERED_LIST = ("ol", "Ordered List")
    UNORDERED_LIST = ("ul", "Unordered List")
    LIST_TYPES = (ORDERED_LIST, UNORDERED_LIST)

    LIST_STYLE_DISC = ("disc", "Disc")
    LIST_STYLE_CIRCLE = ("circle", "Circle")
    LIST_STYLE_SQUARE = ("square", "Square")
    LIST_STYLE_NONE = ("None", "none")
    LIST_STYLE_CHOICES = (LIST_BLANK_CHOICE, LIST_STYLE_DISC, LIST_STYLE_CIRCLE)

    ORDERED_LIST_NUMBERED = ("1", "Numbers")
    ORDERED_LIST_UPPERCASE_LETTERS = ("A", "Uppercase Letters")
    ORDERED_LIST_LOWERCASE_LETTERS = ("a", "Lowercase Letters")
    ORDERED_LIST_ROMAN_NUMERALS = ("I", "Uppercase Roman Numerals")
    ORDERED_LIST_ROMAN_NUMERALS_LC = ("i", "Lowercase Roman Numerals")
    ORDERED_LIST_TYPES = (
        LIST_BLANK_CHOICE,
        ORDERED_LIST_NUMBERED,
        ORDERED_LIST_UPPERCASE_LETTERS,
        ORDERED_LIST_LOWERCASE_LETTERS,
        ORDERED_LIST_ROMAN_NUMERALS,
        ORDERED_LIST_ROMAN_NUMERALS_LC,
    )
    list_type = models.CharField(max_length=10, blank=False, null=False, default=UNORDERED_LIST[0], choices=LIST_TYPES)
    list_style_type = models.CharField(
        max_length=16, blank=True, null=True, default=LIST_BLANK_CHOICE[0], choices=LIST_STYLE_CHOICES
    )
    ordered_list_type = models.CharField(
        max_length=64, blank=True, null=True, default=LIST_BLANK_CHOICE[0], choices=ORDERED_LIST_TYPES
    )
    ordered_list_start = models.IntegerField(blank=True, null=True, default=None)
    attributes = AttributesField()

    def __str__(self):
        return "List %s" % str(self.pk)

    def get_short_description(self):
        return "List %s" % str(self.pk)


class ListItem(CMSPlugin):
    attributes = AttributesField()

    def __str__(self):
        return "List item %s" % str(self.pk)


class PlainTextPlugin(CMSPlugin):
    text = models.TextField(blank=True, null=True)
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    attributes = AttributesField()

    @property
    def class_str(self):
        class_list = []

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)

    def __str__(self):
        return "Plain Text Plugin %s" % str(self.pk)

    def get_short_description(self):

        return "Plain Text Plugin %s" % str(self.pk)


class NavMenuPluginConfig(CMSPlugin):
    title = models.CharField(max_length=200, blank=True, null=True)
    attributes = AttributesField()

    def __str__(self):
        return "Nav Menu Plugin %s" % str(self.pk)

    def get_short_description(self):
        return "Nav Menu Plugin %s" % str(self.title)


class SectionPluginConfig(CMSPlugin):
    title = models.CharField(max_length=200, blank=True, null=True)
    blue_background = models.BooleanField(default=False)
    attributes = AttributesField()

    def __str__(self):
        return "Section Plugin %s" % str(self.pk)

    def get_short_description(self):
        return "Section Plugin %s" % str(self.pk)


class SVGImagePluginConfig(PluginAbstractLink):
    alt_text = models.CharField(max_length=255)
    svg_image = FilerFileField(blank=True, null=True, related_name="svgimage", on_delete=DO_NOTHING)
    attributes = AttributesField()

    def __str__(self):
        retn = "Svg Image: %s" % self.pk

        if self.alt_text:
            retn = "Svg Image: %s" % self.alt_text

        return retn

    def get_short_description(self):
        retn = str(self.pk)

        if self.alt_text:
            retn = self.alt_text

        return retn
