from django.db import models
from django.utils.translation import gettext as _

from commons.models import BaseModel, Tags


class CustomForm (BaseModel):
    name = models.CharField(_("nom"), max_length=50)
    json_schema_form = models.JSONField(_("json schema form"))
    date = models.DateField(_("Date d'ajout"),  auto_now_add=True)
    source = models.URLField(_("Source"), max_length=200)
    tags = models.ManyToManyField("commons.tags", verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("Custom form")
        verbose_name_plural = _("Custom forms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
