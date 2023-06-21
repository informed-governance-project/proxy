# Generated by Django 4.2.1 on 2023-06-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proxy", "0011_remove_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_administrator",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="Administrator",
            ),
        ),
    ]