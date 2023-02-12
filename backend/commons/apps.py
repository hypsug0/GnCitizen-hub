#!/usr/bin/python
# -*- coding: utf-8 -*-
"""GeoNature-Citizen hub commons App config
"""


from django.apps import AppConfig


class CommonsConfig(AppConfig):
    """Commons app config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "commons"
