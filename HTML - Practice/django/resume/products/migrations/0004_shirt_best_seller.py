# Generated by Django 5.0.2 on 2024-05-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_shirt_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
    ]
