# Generated by Django 5.0.2 on 2024-05-19 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
