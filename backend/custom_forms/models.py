from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

from commons.models import BaseModel


class CustomForm(BaseModel):
    name = models.CharField(_("nom"), max_length=50, unique=True)
    json_schema_form = models.JSONField(_("json schema form"))
    date = models.DateField(_("Date d'ajout"), auto_now_add=True)
    source = models.URLField(
        _("Source"), max_length=200, blank=True, null=True
    )
    tags = models.ManyToManyField(
        "commons.tags", verbose_name=_("Tags"), blank=True
    )

    class Meta:
        verbose_name = _("Custom form")
        verbose_name_plural = _("Custom forms")
        unique_together = [["name", "source"]]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
