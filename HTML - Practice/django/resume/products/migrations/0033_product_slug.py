# Generated by Django 5.0.2 on 2024-05-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]