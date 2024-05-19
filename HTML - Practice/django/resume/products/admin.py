from django.contrib import admin
#Import model from current directory, in this cash the Shirt model
from .models import Product, Brand, Address, Category


# Register your models here.


class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","id","best_seller", "brand",)#Removed category
    list_filter = ("best_seller",)
    search_fields = ("title",) 
    #Realized as nice as this is, its overcomplicating unique queries using slugs.
    #prepopulated_fields ={"slug": ("title",)}

class addressAdmin(admin.ModelAdmin):
    list_display =("street","zip_code","city","country",)
    search_fields=("street","zip_code","city","country",)

class categoryAdmin(admin.ModelAdmin):
    list_display=("title","description")

admin.site.register(Category,categoryAdmin)
admin.site.register(Address,addressAdmin)
admin.site.register(Brand)
admin.site.register(Product, productAdmin)