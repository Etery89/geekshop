from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory

# Create your views here.


def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'geekShop - каталог',
        'categories': ProductCategory.objects.all()
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)


# class ProductsListView(ListView):
#     model = Product
#     template_name = 'mainapp/products.html'