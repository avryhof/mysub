from cms.models import CMSPlugin
from django.db import models

from bootstrap4_extensions.constants import BUTTON_CLASSES, BUTTON_SIZES


class BootstrapButton(CMSPlugin):
    label = models.CharField(max_length=150, blank=True, null=True)
    button_class = models.CharField(max_length=20, blank=True, null=True, choices=BUTTON_CLASSES)
    outline_button = models.BooleanField(null=True, default=False)
    button_size = models.CharField(max_length=5, blank=True, null=True, choices=BUTTON_SIZES)
    block_level_button = models.BooleanField(null=True, default=False)
    disable_text_wrapping = models.BooleanField(null=True, default=True)

    class Meta:
        abstract = True

    def get_short_description(self):
        retn = "Button"

        if self.label:
            retn = "Button: %s" % self.label

        return retn
