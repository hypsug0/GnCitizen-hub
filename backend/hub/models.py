from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CitizenInstances(models.Model):
    name = models.CharField(_("Nom"), max_length=50)
    url = models.URLField(_("URL"), max_length=200)
    location = models.PointField(srid=4326)
    is_active = models.BooleanField(_("Actif"))
    launch_date = models.DateField(_("Date de lancement"), auto_now=False, auto_now_add=False)
    project = models.CharField(_("Projet"), max_length=50)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Créé par"), on_delete=models.CASCADE)
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)