# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from shuup.apps import AppConfig


class KingdomSearchAppConfig(AppConfig):
    name = "kingdom_search"
    verbose_name = "Kingdom Search"
    label = "kingdom_search"

    provides = {
        "front_urls": [
            "kingdom_search.urls:urlpatterns"
        ],
        "front_extend_product_list_form": [
            "kingdom_search.forms.FilterProductListByQuery",
        ],
        "front_template_helper_namespace": [
            "kingdom_search.template_helpers:TemplateHelpers"
        ]
    }


default_app_config = "kingdom_search.KingdomSearchAppConfig"
