from django.db import models

# Create your models here.


class profile(models.Model):
    email= models.EmailField()
    full_name= models.CharField(max_length=60)
    dob= models.DateField()