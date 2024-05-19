from django.contrib import admin
#Import model from current directory, in this cash the Shirt model
from .models import Shirt


# Register your models here.

admin.site.register(Shirt)