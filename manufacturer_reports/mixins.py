# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2020, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.db.models import Q

from shuup.core.models import Order
from shuup.utils.dates import to_datetime_range


class ManufacturerOrderReportMixin(object):
    def get_objects(self):
        (start, end) = to_datetime_range(self.start_date, self.end_date)
        queryset = Order.objects.filter(
            shop=self.shop, order_date__range=(start, end))
        creator = self.options.get("creator")
        orderer = self.options.get("orderer")
        manufacturer = self.options.get("manufacturer")
        filters = Q()
        if creator:
            filters &= Q(creator__in=creator)
        if orderer:
            filters &= Q(orderer__in=orderer)
        if manufacturer:
            filters &= Q(lines__product__manufacturer__in=manufacturer)

        return queryset.filter(filters).valid().paid().order_by("order_date").prefetch_related('lines__product')
