# Generated by Django 5.0.2 on 2024-05-19 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
