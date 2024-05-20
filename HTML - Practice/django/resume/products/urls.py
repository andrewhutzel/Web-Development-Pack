from django.urls import path
from . import views

#Connects to urls.py under products directory

#Based on requests to website (EX: 0.0.0.0:8000/website_function) that is derived from urlpatterns

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    #Uncomment below to make Example work
    #path('website_function',views.index),
    path('products/<product>',views.product_category,name="product_category"),
    path('signup.html',views.signup, name="signup"),
    path('products/<product_brand>/<product_slug>', views.ProductPageView.as_view(), name="product_page")
    #path('products/<product_brand>/', views.product_page, name="product_page")
]
