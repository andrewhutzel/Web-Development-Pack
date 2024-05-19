from django.urls import path
from . import views

#Connects to urls.py under products directory

#Based on requests to website (EX: 0.0.0.0:8000/website_function) that is derived from urlpatterns

urlpatterns = [
    path('', views.index, name="home"),
    #Uncomment below to make Example work
    #path('website_function',views.index),
    path('products/<product>',views.product_category,name="product_category"),
    path('signup.html',views.signup, name="signup"),
]
