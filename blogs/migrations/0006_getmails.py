# Generated by Django 4.2.7 on 2023-12-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0005_stories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Getmails",
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
                ("email", models.EmailField(max_length=255)),
            ],
        ),
    ]
