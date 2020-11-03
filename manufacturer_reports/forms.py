# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2020, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django import forms
from django.utils.translation import ugettext_lazy as _

from shuup.admin.forms.fields import Select2MultipleField
from shuup.core.models import Contact, Manufacturer
from shuup.reports.forms import BaseReportForm


class ManufacturerOrderReportForm(BaseReportForm):

    def __init__(self, *args, **kwargs):
        super(ManufacturerOrderReportForm, self).__init__(*args, **kwargs)

        manufacturer_field = Select2MultipleField(label=_("Manufacturer"),
                                              model=Manufacturer,
                                              required=False,
                                              help_text=_("Filter report results by manufacturer."))
        manufacturers = self.initial_manufacturers("manufacturer")
        if manufacturers:
            manufacturer_field.initial = manufacturers
            manufacturer_field.widget.choices = [(obj.pk, obj.name) for obj in manufacturers]
        orderer_field = Select2MultipleField(
            label=_("Orderer"), model=Contact, required=False, help_text=_(
                "Filter report results by the person that made the order."
            )
        )
        orderers = self.initial_manufacturers("orderer")
        if orderers:
            orderer_field.initial = orderers
            orderer_field.widget.choices = [(obj.pk, obj.name) for obj in orderers]
        self.fields["manufacturer"] = manufacturer_field
        self.fields["orderer"] = orderer_field

    def initial_manufacturers(self, key):
        if self.data and key in self.data:
            return Manufacturer.objects.filter(pk__in=self.data.getlist(key))
        return []

#
# class CustomerSalesReportForm(OrderReportForm):
#     SORT_ORDER_CHOICES = (
#         ("order_count", _("Order Count")),
#         ("average_sales", _("Average Sales")),
#         ("taxless_total", _("Taxless Total")),
#         ("taxful_total", _("Taxful Total")),
#     )
#     order_by = forms.ChoiceField(label=_("Sort order"),
#                                  initial="order_count",
#                                  required=True,
#                                  choices=SORT_ORDER_CHOICES)
