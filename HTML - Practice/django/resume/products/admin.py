from django.contrib import admin
#Import model from current directory, in this cash the Shirt model
from .models import Shirt, Product


# Register your models here.


class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","id","category","best_seller",)
    list_filter = ("best_seller",)
    search_fields = ("title","category")

admin.site.register(Shirt)
admin.site.register(Product, productAdmin)