from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from . import app_name
from .models import (
    DIVPluginConfig,
    List,
    ListItem,
    SectionPluginConfig,
    NavMenuPluginConfig,
    SVGImagePluginConfig,
    BlockTagPluginConfig,
    ExpanderPluginConfig,
    HeadingPluginConfig,
    AuthenticatedUserPluginConfig, PlainTextPluginConfig,
)


class AuthenticatedUserPlugin(CMSPluginBase):
    model = AuthenticatedUserPluginConfig
    name = _("Authenticated User Content")
    render_template = "authenticated-user-content.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(AuthenticatedUserPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(AuthenticatedUserPlugin)


class BlockTagPlugin(CMSPluginBase):
    model = BlockTagPluginConfig
    name = _("Block Tag")
    render_template = "block-tag-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(BlockTagPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(BlockTagPlugin)


class DIVPlugin(CMSPluginBase):
    model = DIVPluginConfig
    name = _("DIV Plugin")
    render_template = "div-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(DIVPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(DIVPlugin)


class ExpanderPlugin(CMSPluginBase):
    model = ExpanderPluginConfig
    name = _("Expander Plugin")
    render_template = "expander-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ExpanderPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ExpanderPlugin)


class HeadingPlugin(CMSPluginBase):
    model = HeadingPluginConfig
    name = _("Heading")
    render_template = "heading-plugin.html"
    allow_children = False
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(HeadingPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(HeadingPlugin)


class ListPlugin(CMSPluginBase):
    model = List
    name = _("List")
    render_template = "list-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ListPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ListPlugin)


class ListItemPlugin(CMSPluginBase):
    model = ListItem
    name = _("List Item")
    render_template = "list-item-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ListItemPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ListItemPlugin)


class NavMenuPlugin(CMSPluginBase):
    model = NavMenuPluginConfig
    name = _("Nav Menu (CMS)")
    render_template = "cms-menu.html"
    allow_children = False
    module = _(app_name)


plugin_pool.register_plugin(NavMenuPlugin)


class PlainTextPlugin(CMSPluginBase):
    model = PlainTextPluginConfig
    name = _("Plain Text")
    render_template = "plain-text-plugin.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(PlainTextPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(PlainTextPlugin)


class SectionPlugin(CMSPluginBase):
    model = SectionPluginConfig
    name = _("Section Plugin")
    render_template = "section-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(SectionPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(SectionPlugin)


class SVGImagePluginAdminForm(ModelForm):
    class Meta:
        model = SVGImagePluginConfig
        fields = [
            "svg_image",
            "alt_text",
            "link",
            "attributes",
        ]


class SVGImagePlugin(CMSPluginBase):
    model = SVGImagePluginConfig
    name = _("SVG Image")
    form = SVGImagePluginAdminForm
    render_template = "svg-image-plugin.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super(SVGImagePlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(SVGImagePlugin)
