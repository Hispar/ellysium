# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "kingdomtheme"
    label = "kingdomtheme"
    provides = {
        "xtheme": "kingdomtheme.theme:KingdomWargamesTheme",
    }
