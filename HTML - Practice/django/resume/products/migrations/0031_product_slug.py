# Generated by Django 5.0.2 on 2024-05-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_remove_product_slug_alter_product_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
