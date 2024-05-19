from django.db import models

# Create your models here.

#Find all types of models here https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Shirt(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()