# Generated by Django 5.0.2 on 2024-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name=models.AutoField(primary_key=True)),
        ),
    ]