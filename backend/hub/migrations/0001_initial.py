# Generated by Django 3.2.3 on 2021-05-26 21:34

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CitizenInstances",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nom")),
                ("url", models.URLField(verbose_name="URL")),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                ("is_active", models.BooleanField(verbose_name="Actif")),
                (
                    "launch_date",
                    models.DateField(verbose_name="Date de lancement"),
                ),
                (
                    "project",
                    models.CharField(max_length=50, verbose_name="Projet"),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Créé par",
                    ),
                ),
            ],
        ),
    ]
