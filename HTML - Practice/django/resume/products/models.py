from django.db import models

# Create your models here.

#Find all types of models here https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Category(models.Model):
    title = models.CharField(max_length=50)
    description= models.TextField()

    def __str__(self):
        return f"{self.title}"
    

class Address(models.Model):
    street=models.CharField(max_length=200)
    zip_code=models.PositiveIntegerField()
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street} - {self.city}"

class Brand(models.Model):
    title= models.CharField(max_length=50)
    logo= models.ImageField(blank=True, upload_to='brand-img')
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.title}"
    

    
class Product(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank=True, upload_to='product-img')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name="products")
    price = models.FloatField()
    slug = models.SlugField(blank=True)
    best_seller = models.BooleanField(default=False)
    #Make a connection for other products here
    suggestions = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.title}"
    

  
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.slug = self.id
        super().save(*args,**kwargs)