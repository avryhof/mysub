from cms.models import CMSPlugin
from django.db import models
from django.db.models import DO_NOTHING
from djangocms_attributes_field.fields import AttributesField
from filer.fields.file import FilerFileField

from bootstrap4_extensions.constants import (
    NAV_STYLE_CHOICES,
    NAV_ALIGNMENT_CHOICES,
    CONTENT_START,
    NAVBAR_BACKGROUND_SCHEME,
    NAVBAR_DARK,
    NAVBAR_POSITIONS,
    MODAL_TRIGGER_TYPES,
    BUTTON_CLASSES,
    BUTTON_SIZES,
)
from cms_plugins.constants import BACKGROUND_CLASSES, TEXT_CLASSES
from cms_plugins.models_abstract import PluginAbstractLink


class HTML5Video(CMSPlugin):
    SIXTEEN_BY_NINE = "Widescreen 16x9"
    FOUR_BY_THREE = "Full/square Screen 4x3"
    SIXTEENBYNINE = "16by9"
    FOURBYTHREE = "4by3"
    ASPECT_RATIO_CHOICES = (
        (SIXTEEN_BY_NINE, SIXTEENBYNINE),
        (FOUR_BY_THREE, FOURBYTHREE),
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    video_file = FilerFileField(related_name="html5_video_file", blank=True, null=True, on_delete=DO_NOTHING)
    aspect_ratio = models.CharField(max_length=25, default=SIXTEEN_BY_NINE, choices=ASPECT_RATIO_CHOICES)
    attributes = AttributesField()

    def __str__(self):
        return self.title

    def get_short_description(self):
        return self.title or self.video_file.url


class ModalTriggerConfig(CMSPlugin):
    label = models.CharField(max_length=200, blank=True, null=True)
    trigger_type = models.CharField(max_length=50, null=False, default="button", choices=MODAL_TRIGGER_TYPES)
    target = models.CharField(max_length=50, blank=True, null=True)
    button_class = models.CharField(max_length=50, blank=True, null=True, choices=BUTTON_CLASSES)
    button_size = models.CharField(max_length=50, blank=True, null=True, choices=BUTTON_SIZES)
    additional_css_classes = models.CharField(
        max_length=200, blank=True, null=True, help_text="Space separated. Example: nav-link text-success"
    )

    def __str__(self):
        return "Modal Trigger %s" % self.target

    def get_short_description(self):
        return "Modal Trigger %s" % self.target

    @property
    def class_str(self):
        class_list = []

        if self.trigger_type == "button":
            class_list.append("btn")

            if self.button_class:
                class_list.append(self.button_class)

            if self.button_size:
                class_list.append(self.button_size)

        if self.additional_css_classes:
            class_list = class_list + self.additional_css_classes.split(" ")

        return " ".join(class_list)


class ModalPluginConfig(CMSPlugin):
    target_name = models.CharField(max_length=200, blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    static_backdrop = models.BooleanField(
        default=False, help_text="When backdrop is set to static, the modal will not close when clicking outside it."
    )
    vertically_centered = models.BooleanField(default=False)
    scrollable = models.BooleanField(default=False)

    def get_short_description(self):
        return "Modal %s" % self.target_name


class ModalBodyPluginConfig(CMSPlugin):
    pass


class ModalFooterPluginConfig(CMSPlugin):
    additional_css_classes = models.CharField(
        max_length=200, blank=True, null=True, help_text="Space separated. Example: text-right"
    )

    @property
    def class_str(self):
        class_list = ["modal-footer"]

        if self.additional_css_classes:
            class_list = class_list + self.additional_css_classes.split(" ")

        return " ".join(class_list)


class ModalCloseButtonPluginConfig(CMSPlugin):
    label = models.CharField(max_length=200, default="Close")
    button_class = models.CharField(max_length=50, null=True, choices=BUTTON_CLASSES)
    button_size = models.CharField(max_length=50, null=True, choices=BUTTON_SIZES)
    additional_css_classes = models.CharField(
        max_length=200, blank=True, null=True, help_text="Space separated. Example: text-right"
    )

    @property
    def class_str(self):
        class_list = ["btn"]

        if self.button_class:
            class_list.append(self.button_class)

        if self.button_size:
            class_list.append(self.button_size)

        if self.additional_css_classes:
            class_list = class_list + self.additional_css_classes.split(" ")

        return " ".join(class_list)


class NavBarPluginConfig(CMSPlugin):
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, default="bg-dark")
    background_scheme = models.CharField(max_length=50, choices=NAVBAR_BACKGROUND_SCHEME, default=NAVBAR_DARK)
    navbar_position = models.CharField(max_length=50, blank=True, choices=NAVBAR_POSITIONS, default="")
    attributes = AttributesField()

    @property
    def class_str(self):
        class_list = [
            "navbar",
            self.background_scheme,
            self.background_class,
            self.navbar_position,
        ]

        return " ".join(class_list)


class NavBarBrandPluginConfig(PluginAbstractLink):
    attributes = AttributesField()

    def __str__(self):
        retn = "Navbar Brand: %s" % self.get_link

        return retn


class NavPluginConfig(CMSPlugin):
    style = models.CharField(max_length=50, blank=True, choices=NAV_STYLE_CHOICES, default="")
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, default="bg-dark")
    horizontal_alignment = models.CharField(max_length=50, choices=NAV_ALIGNMENT_CHOICES, default=CONTENT_START)
    vertical_desktop = models.BooleanField(default=False)
    vertical_mobile = models.BooleanField(default=False)

    @property
    def class_str(self):
        class_list = ["nav", self.background_class]

        if self.style:
            class_list.append(self.style)

        if self.horizontal_alignment:
            class_list.append(self.horizontal_alignment)

        if self.vertical_desktop:
            class_list.append("flex-column")

        if self.vertical_mobile:
            class_list.append("flex-sm-column")

        return " ".join(class_list)

    def __str__(self):
        return "Nav %s" % str(self.pk)

    def get_short_description(self):
        return "Nav %s" % str(self.pk)


class NavItem(CMSPlugin):
    dropdown = models.BooleanField(default=False, null=False)
    attributes = AttributesField()

    def __str__(self):
        return "NavItem item %s" % str(self.pk)


class NavLinkPluginConfig(PluginAbstractLink):
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    dropdown = models.BooleanField(default=False, null=False)
    attributes = AttributesField()

    @property
    def class_str(self):
        class_list = ["nav-link"]

        if self.dropdown:
            class_list.append("dropdown-toggle")

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)

    def __str__(self):
        retn = "Nav Link: %s" % self.get_link

        if self.title:
            retn = "Nav Link: %s" % self.title

        return retn


class NavDropDownMenuConfig(CMSPlugin):
    text_class = models.CharField(max_length=50, choices=TEXT_CLASSES, blank=True, null=True)
    background_class = models.CharField(max_length=50, choices=BACKGROUND_CLASSES, blank=True, null=True)
    attributes = AttributesField()

    @property
    def class_str(self):
        class_list = ["dropdown-menu"]

        if self.text_class:
            class_list.append(self.text_class)

        if self.background_class:
            class_list.append(self.background_class)

        return " ".join(class_list)


class NavDropDownItemConfig(PluginAbstractLink):
    pass


class NavDropDownDividerConfig(CMSPlugin):
    pass
