from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
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
        abstract = True


class Tags(BaseModel):

    label = models.CharField(_("Label"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
