# Generated by Django 4.2.1 on 2023-05-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transfers", "0002_rename_total_to_transfer_transfer_total_to_pay"),
    ]

    operations = [
        migrations.AddField(
            model_name="transfer",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
