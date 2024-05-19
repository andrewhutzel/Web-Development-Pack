from django.shortcuts import render
#Exclusively added to index function test
from django.http import HttpResponse
from .models import Product


# Create your views here.

#Function created to demonstrate django is running and we can modify

def index(request):
    user = "eest"
    products_num=4
    products = Product.objects.all().order_by('-id')[:4]
    return render(request, "products/home.html", {
        "name":user,
        "products_num":products_num,
        "products":products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_category(request,product):
    if(product == "Suits" or product == "Shirts" or product == "Shoes" or product == "Dress" ):
        return HttpResponse(f"Here is a list of our suits {product}")
    return HttpResponse(f"This list is not supported!")