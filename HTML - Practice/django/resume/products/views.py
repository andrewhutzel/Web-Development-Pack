from django.shortcuts import render
#Exclusively added to index function test
from django.http import HttpResponse
from .models import Product, Brand
from django.contrib import messages

from .forms import FeedbackForm


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

def product_page(request,product_brand,product_slug):
    product = Product.objects.get(slug= product_slug)
    form = FeedbackForm()
    
    if(request.method == "GET"):
        return render(request,"products/product.html",{
        "product":product,
        "form":form,
        })
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            messages.success(request, "Feedback was successfully submitted.")
            form = FeedbackForm()
        #result = request.POST["username"]
        return render(request,"products/product.html",{
        "product":product,
        "form":form,
        })