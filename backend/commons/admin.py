#!/usr/bin/python
# -*- coding: utf-8 -*-
"""GeoNature-Citizen hub commons admin
"""


from django.contrib import admin

from .models import Tags

# Register your models here.


admin.site.register(Tags, admin.ModelAdmin)
