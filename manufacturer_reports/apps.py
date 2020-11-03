# This file is part of Shuup.
#
# Copyright (c) 2012-2020, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "manufacturer_reports"
    provides = {
        "reports": [
            "manufacturer_reports.reports.sales:ManufacturerSalesReport",
            # "shuup.default_reports.reports.customer_sales:CustomerSalesReport",
        ],
    }
