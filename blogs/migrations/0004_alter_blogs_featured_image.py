# Generated by Django 4.2.7 on 2023-12-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_alter_blogs_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="featured_image",
            field=models.ImageField(upload_to="media/blogs/image"),
        ),
    ]