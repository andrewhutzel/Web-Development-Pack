# Generated by Django 5.0.2 on 2024-05-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggestions',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]