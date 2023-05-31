# Generated by Django 4.2.1 on 2023-05-31 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("governanceplatform", "0006_alter_sectoradministration_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sector",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="governanceplatform.sector",
            ),
        ),
    ]