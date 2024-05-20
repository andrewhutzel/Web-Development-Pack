from django.shortcuts import redirect, render
#Exclusively added to index function test
from django.http import HttpResponse
from .models import Product, Feedback
from django.contrib import messages
from django.views import View

from .forms import FeedbackForm


# Create your views here.

#Function created to demonstrate django is running and we can modify

class IndexView(View):
    def get(self,request):
        user = "eest"
        products_num=4
        products = Product.objects.all().order_by('-id')[:4]

        return render(request, "products/home.html", {
            "name":user,
            "products_num":products_num,
            "products":products,
        })
    def post(self,request):
        pass

#def index(request):
#    user = "eest"
#    products_num=4
#    products = Product.objects.all().order_by('-id')[:4]
#
#    return render(request, "products/home.html", {
#        "name":user,
#        "products_num":products_num,
#        "products":products,
#    })

def signup(request):
    return render(request, "products/signup.html")

def product_category(request,product):
    if(product == "Suits" or product == "Shirts" or product == "Shoes" or product == "Dress" ):
        return HttpResponse(f"Here is a list of our suits {product}")
    return HttpResponse(f"This list is not supported!")


class ProductPageView(View):
    def get(self,request,product_brand,product_slug):
        product = Product.objects.get(slug= product_slug)
        my_feedback=Feedback.objects.get(product=product,id=75)
        form = FeedbackForm(instance = my_feedback)
        reviews=Feedback.objects.filter(product = product)
        return render(request,"products/product.html",{
            "product":product,
            "form":form,
            "reviews":reviews
        })
    def post(self,request,product_brand,product_slug):
        product = Product.objects.get(slug= product_slug)
        my_feedback=Feedback.objects.get(product=product,id=75)
        form = FeedbackForm(instance = my_feedback)
        reviews=Feedback.objects.filter(product = product)
        form = FeedbackForm(request.POST, instance = my_feedback)
        if form.is_valid():
            form.save()
            
            #feeback = Feedback(
            #    name=form.cleaned_data["name"],
            #   rating=form.cleaned_data["rating"],
            #    text = form.cleaned_data["text"],
            #    product=product,
            #).save()
            messages.success(request, "Feedback was successfully submitted.")
            #Clears the form
            form = FeedbackForm()
            #Only thing preventing spamming of feedback input...
            #return redirect('home')
        #result = request.POST["username"]
        return render(request,"products/product.html",{
            "product":product,
            "form":form,
            "reviews":reviews
        })
'''
def product_page(request,product_brand,product_slug):
    product = Product.objects.get(slug= product_slug)
    
    my_feedback=Feedback.objects.get(product=product,id=75)
    
    form = FeedbackForm(instance = my_feedback)
    
    reviews=Feedback.objects.filter(product = product)


    if(request.method == "GET"):
        return render(request,"products/product.html",{
        "product":product,
        "form":form,
        "reviews":reviews
        })
    else:
        form = FeedbackForm(request.POST, instance = my_feedback)
        if form.is_valid():
            form.save()
            
            #feeback = Feedback(
            #    name=form.cleaned_data["name"],
            #   rating=form.cleaned_data["rating"],
            #    text = form.cleaned_data["text"],
            #    product=product,
            #).save()
            messages.success(request, "Feedback was successfully submitted.")
            #Clears the form
            form = FeedbackForm()
            #Only thing preventing spamming of feedback input...
            #return redirect('home')
        #result = request.POST["username"]
        return render(request,"products/product.html",{
        "product":product,
        "form":form,
        "reviews":reviews
        })
'''