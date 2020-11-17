from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from . import app_name
from .models import BannerSectionPluginConfig, SectionHeaderPluginConfig, PortfolioItemPluginConfig, TopBarPluginConfig


class BannerSectionPlugin(CMSPluginBase):
    model = BannerSectionPluginConfig
    name = _("Banner Section (animated)")
    render_template = "banner-section.html"
    allow_children = False
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(BannerSectionPlugin, self).render(context, instance, placeholder)

        context["words"] = '["%s"]' % '","'.join(instance.rotate_words)

        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(BannerSectionPlugin)


class PortfolioItemPlugin(CMSPluginBase):
    model = PortfolioItemPluginConfig
    name = _("Portfolio Item")
    render_template = "portfolio-item.html"
    allow_children = False
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(PortfolioItemPlugin, self).render(context, instance, placeholder)

        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(PortfolioItemPlugin)


class SectionHeaderPlugin(CMSPluginBase):
    model = SectionHeaderPluginConfig
    name = _("Section Header")
    render_template = "section-header.html"
    allow_children = False
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(SectionHeaderPlugin, self).render(context, instance, placeholder)

        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(SectionHeaderPlugin)


class TopBarPlugin(CMSPluginBase):
    model = TopBarPluginConfig
    name = _("Top Bar")
    render_template = "top-bar.html"
    allow_children = False
    module = _("Unicat")

    def render(self, context, instance, placeholder):
        context = super(TopBarPlugin, self).render(context, instance, placeholder)

        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(TopBarPlugin)
