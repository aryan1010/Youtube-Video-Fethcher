# Generated by Django 5.0.3 on 2024-03-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="APIKey",
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
                ("key", models.CharField(max_length=100, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
