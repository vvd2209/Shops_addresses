# Generated by Django 5.0.7 on 2024-07-20 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название города"),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Street",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название улицы"),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Улица",
                "verbose_name_plural": "Улицы",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Shop",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название магазина"),
                ),
                ("house", models.IntegerField(verbose_name="Дом")),
                ("opening_time", models.TimeField(verbose_name="Время открытия")),
                ("closing_time", models.TimeField(verbose_name="Время закрытия")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.city",
                        verbose_name="Город",
                    ),
                ),
                (
                    "street",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.street",
                        verbose_name="Улица",
                    ),
                ),
            ],
            options={
                "verbose_name": "Магазин",
                "verbose_name_plural": "Магазины",
                "ordering": ("name",),
            },
        ),
    ]