# Generated by Django 3.2.3 on 2022-02-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commons", "0002_alter_tags_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tags",
            name="label",
            field=models.CharField(max_length=50, unique=True, verbose_name="Label"),
        ),
    ]