# Generated by Django 4.2.1 on 2023-05-22 23:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0003_alter_newspaper_published_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newspaper",
            name="redactor",
        ),
        migrations.AddField(
            model_name="newspaper",
            name="redactors",
            field=models.ManyToManyField(
                related_name="newspapers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]