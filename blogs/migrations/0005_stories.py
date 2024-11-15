# Generated by Django 4.2.7 on 2023-12-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_alter_blogs_featured_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stories",
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
                ("name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("content", models.CharField(max_length=565)),
                ("isfemale", models.BooleanField(default=False)),
            ],
        ),
    ]
