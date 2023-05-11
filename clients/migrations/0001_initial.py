# Generated by Django 4.2.1 on 2023-05-11 13:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(default="", max_length=40)),
                ("last_name", models.CharField(default="", max_length=90)),
                (
                    "birthday",
                    models.DateField(
                        default=datetime.datetime(
                            2023,
                            5,
                            11,
                            13,
                            20,
                            58,
                            912555,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientFriend",
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
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_client",
                        to="clients.client",
                    ),
                ),
                (
                    "friend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_friend",
                        to="clients.client",
                    ),
                ),
            ],
        ),
    ]