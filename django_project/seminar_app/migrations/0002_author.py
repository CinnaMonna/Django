# Generated by Django 5.0.1 on 2024-01-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seminar_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("bio", models.TextField()),
                ("birthday", models.DateField()),
            ],
        ),
    ]