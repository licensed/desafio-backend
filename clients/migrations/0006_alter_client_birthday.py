# Generated by Django 4.2.1 on 2023-05-11 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0005_alter_client_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="birthday",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 5, 11, 14, 8, 15, 447117, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
