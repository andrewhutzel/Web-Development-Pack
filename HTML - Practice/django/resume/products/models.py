from django.db import models

# Create your models here.

#Find all types of models here https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Shirt(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    best_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
class Product(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField(blank=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='product-img')
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    slug = models.SlugField(blank=True)
    best_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.slug = self.id
        super().save(*args,**kwargs)
