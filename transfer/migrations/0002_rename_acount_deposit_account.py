# Generated by Django 4.1.5 on 2023-01-09 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transfer", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deposit",
            old_name="acount",
            new_name="account",
        ),
    ]
