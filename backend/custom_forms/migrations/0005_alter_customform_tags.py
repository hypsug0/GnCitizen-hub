# Generated by Django 4.1.6 on 2023-02-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commons", "0003_alter_tags_label"),
        ("custom_forms", "0004_auto_20220219_2048"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customform",
            name="tags",
            field=models.ManyToManyField(blank=True, to="commons.tags", verbose_name="Tags"),
        ),
    ]