# Generated by Django 4.2.7 on 2023-12-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0006_getmails"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogs",
            name="meta_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="blogs",
            name="meta_keywords",
            field=models.TextField(
                blank=True, help_text="use comma( , ) for separation", null=True
            ),
        ),
        migrations.AddField(
            model_name="blogs",
            name="meta_title",
            field=models.CharField(
                blank=True,
                help_text="if leave it will take from title ",
                max_length=255,
                null=True,
            ),
        ),
    ]
