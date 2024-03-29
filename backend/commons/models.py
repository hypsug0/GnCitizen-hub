#!/usr/bin/python
# -*- coding: utf-8 -*-
"""GeoNature-Citizen hub commons models
"""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.


class BaseModel(
    models.Model
):  # base class should subclass 'django.db.models.Model'
    """Common shared base model with metadata fields"""

    timestamp_create = models.DateTimeField(
        _("Create timestamp"), auto_now_add=True, editable=False
    )
    timestamp_update = models.DateTimeField(
        _("Update timestamp"), auto_now=True, editable=False
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    class Meta:
        """Base model Meta class"""

        abstract = True


class Tags(BaseModel):
    """Tags model"""

    label = models.CharField(
        _("Label"), unique=True, max_length=50, null=False, blank=False
    )

    class Meta:
        """Tags model Meta class"""

        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
