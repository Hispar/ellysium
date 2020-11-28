# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.conf.urls import url

from django.views.decorators.csrf import csrf_exempt

from .views.category import CategoryView

urlpatterns = [
    url(r'^category/(?P<pk>\d+)-(?P<slug>.*)/$',
        csrf_exempt(CategoryView.as_view()),
        name='category-kingdom'),
]
