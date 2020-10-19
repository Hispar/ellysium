# -*- coding: utf-8 -*-
# Python imports

# Django imports
import django.conf
from django import forms
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

# 3rd Party imports
from shuup.xtheme import Theme


# App imports


class KingdomWargamesTheme(Theme):
    identifier = "kingdomtheme"
    name = "Kingdom Wargames Theme"
    author = "Hispar"
    template_dir = "kingdomtheme"

    fields = [
        ("show_welcome_text", forms.BooleanField(required=False, initial=True, label=_("Show Frontpage Welcome Text"))),
        ("hide_prices", forms.BooleanField(required=False, initial=False, label=_("Hide prices"))),
        ("catalog_mode", forms.BooleanField(required=False, initial=False, label=_("Set shop in catalog mode"))),
        (
            "show_supplier_info",
            forms.BooleanField(
                required=False, initial=False, label=_("Show supplier info"),
                help_text=_("Show supplier name in product-box, product-detail, basket- and order-lines"))
        )
    ]

    guide_template = "kingdomtheme/admin/guide.jinja"

    stylesheets = [
        {
            "identifier": "kingdomtheme",
            "stylesheet": "shuup/front/css/style.css",
            "name": _("Kingdom Wargames"),
            "images": ["shuup/front/img/no_image.png"]
        }
    ]

    def get_view(self, view_name):
        import shuup.front.themes.views as views
        return getattr(views, view_name, None)

    def _format_cms_links(self, shop, **query_kwargs):
        if "shuup.simple_cms" not in django.conf.settings.INSTALLED_APPS:
            return
        from shuup.simple_cms.models import Page
        for page in Page.objects.visible(shop).filter(**query_kwargs):
            yield {"url": "/%s" % page.url, "text": force_text(page)}

    def get_cms_navigation_links(self, request):
        return self._format_cms_links(shop=request.shop, visible_in_menu=True)
