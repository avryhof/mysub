from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from bootstrap4_extensions import app_name
from bootstrap4_extensions.models import (
    HTML5Video,
    NavPluginConfig,
    NavItem,
    NavLinkPluginConfig,
    NavDropDownMenuConfig,
    NavDropDownItemConfig,
    NavDropDownDividerConfig,
    NavBarPluginConfig,
    NavBarBrandPluginConfig,
    ModalTriggerConfig,
    ModalPluginConfig,
    ModalBodyPluginConfig,
    ModalFooterPluginConfig,
    ModalCloseButtonPluginConfig,
)


class HTML5VideoPlugin(CMSPluginBase):
    model = HTML5Video
    name = _("HTML5 Video")
    render_template = "html5_video.html"
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(HTML5VideoPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(HTML5VideoPlugin)


class ModalPlugin(CMSPluginBase):
    model = ModalPluginConfig
    name = _("Modal Dialog")
    render_template = "modal-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ModalPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ModalPlugin)


class ModalBodyPlugin(CMSPluginBase):
    model = ModalBodyPluginConfig
    name = _("Modal Body")
    render_template = "modal-body-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ModalBodyPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ModalBodyPlugin)


class ModalCloseButtonPlugin(CMSPluginBase):
    model = ModalCloseButtonPluginConfig
    name = _("Modal Close Button")
    render_template = "modal-close-button-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ModalCloseButtonPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ModalCloseButtonPlugin)


class ModalFooterPlugin(CMSPluginBase):
    model = ModalFooterPluginConfig
    name = _("Modal Footer")
    render_template = "modal-footer-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ModalFooterPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ModalFooterPlugin)


class ModalTriggerPlugin(CMSPluginBase):
    model = ModalTriggerConfig
    name = _("Modal Trigger")
    render_template = "modal-trigger-plugin.html"
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(ModalTriggerPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(ModalTriggerPlugin)


class NavBarPlugin(CMSPluginBase):
    model = NavBarPluginConfig
    name = _("Nav Bar")
    render_template = "nav-bar-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavBarPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavBarPlugin)


class NavBarBrandPlugin(CMSPluginBase):
    model = NavBarBrandPluginConfig
    name = _("Nav Bar Brand")
    render_template = "nav-bar-brand-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavBarBrandPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavBarBrandPlugin)


class NavPlugin(CMSPluginBase):
    model = NavPluginConfig
    name = _("Nav")
    render_template = "nav-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavPlugin)


class NavItemPlugin(CMSPluginBase):
    model = NavItem
    name = _("Nav Item")
    render_template = "nav-item-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavItemPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavItemPlugin)


class NavLinkPlugin(CMSPluginBase):
    model = NavLinkPluginConfig
    name = _("Nav Link")
    render_template = "nav-link-plugin.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavLinkPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavLinkPlugin)


class NavDropDownMenuPlugin(CMSPluginBase):
    model = NavDropDownMenuConfig
    name = _("Dropdown Menu")
    render_template = "nav-dropdown-menu.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavDropDownMenuPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavDropDownMenuPlugin)


class NavDropDownItemPlugin(CMSPluginBase):
    model = NavDropDownItemConfig
    name = _("Dropdown Item")
    render_template = "nav-dropdown-item.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavDropDownItemPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavDropDownItemPlugin)


class NavDropDownDividerPlugin(CMSPluginBase):
    model = NavDropDownDividerConfig
    name = _("Dropdown Divider")
    render_template = "nav-dropdown-divider.html"
    allow_children = True
    module = _(app_name)

    def render(self, context, instance, placeholder):
        context = super(NavDropDownDividerPlugin, self).render(context, instance, placeholder)
        context.update({"instance": instance})

        return context


plugin_pool.register_plugin(NavDropDownDividerPlugin)
