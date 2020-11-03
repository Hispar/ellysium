# -*- coding: utf-8 -*-
# Python imports
import itertools

# Django imports

# 3rd Party imports

# App imports

from babel.dates import format_date
from django.db.models import Sum
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from shuup.core.models import Product

from shuup.reports.report import ShuupReportBase
from shuup.utils.i18n import get_current_babel_locale

from manufacturer_reports.forms import ManufacturerOrderReportForm
from manufacturer_reports.mixins import ManufacturerOrderReportMixin


class ManufacturerSalesReport(ManufacturerOrderReportMixin, ShuupReportBase):
    identifier = "manufacturer_sales_report"
    title = _("Manufacturer Sales Report")
    form_class = ManufacturerOrderReportForm

    filename_template = "manufacturer-sales-report-%(time)s"
    schema = [
        {"key": "product_id", "title": _("SKU")},
        {"key": "product_name", "title": _("Product Name")},
        {"key": "product_count", "title": _("Quantity")},
    ]

    def extract_date(self, entity):
        return localtime(entity.order_date).date()

    def get_data(self):
        orders = self.get_objects().order_by("-order_date")
        data = []

        products = Product.objects.filter(order_lines__in=orders.values_list('lines', flat=True)).annotate(
            num_products=Sum('order_lines__quantity'))
        # TODO: maybe make raw sql query in future
        for product in products:
            data.append({
                "product_id": product.sku,
                "product_count": int(product.num_products),
                "product_name": product.name,
            })

        return self.get_return_data(data)
