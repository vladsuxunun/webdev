from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render
from . models import Category,Product

def index(request):
    return render(request,'api/main.html')

def categories(request):
    categories_list = Category.objects.order_by('name')
    return render(request, 'api/categories.html', {'categories_list': categories_list})

def products(request):
    products_list=Product.objects.order_by('name')
    return render(request,'api/products.html',{'products_list':products_list})

def product_details(request, product_id):
    try:
        prod=Product.objects.get(id=product_id)
    except:
        raise Http404("NO PRODUCT(((")

    return render(request,'api/product_details.html',{'product':prod})

def category_details(request, category_id):
    try:
        cat=Category.objects.get(id=category_id)
    except:
        raise Http404("NO CATEGORY(((")
    return render(request,'api/category_details.html',{'category':cat})

def categories_products(request, category_id):
    try:
        categories_products = Product.objects.filter(category_id = category_id)
    except:
        raise Http404("NO PRODUCTS(((")
    return render(request,'api/categories_products.html', {'categories_products':categories_products})
