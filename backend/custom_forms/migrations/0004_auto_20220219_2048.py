# Generated by Django 3.2.3 on 2022-02-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commons", "0003_alter_tags_label"),
        ("custom_forms", "0003_auto_20220219_2039"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customform",
            name="source",
            field=models.URLField(
                blank=True, null=True, verbose_name="Source"
            ),
        ),
        migrations.AlterField(
            model_name="customform",
            name="tags",
            field=models.ManyToManyField(
                blank=True, null=True, to="commons.Tags", verbose_name="Tags"
            ),
        ),
    ]
