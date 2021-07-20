from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.conf import settings
from django.core.cache import cache

from mainapp.models import Product, ProductCategory

# Create your views here.


def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


def get_categories():
    if settings.LOW_CACHE:
        key = 'categories'
        categories = cache.get(key)
        if categories is None:
            categories = ProductCategory.objects.all()
            cache.set(key, categories)
        return categories
    else:
        return ProductCategory.objects.all()


def products(request, category_id=None, page=1):
    context = {
        'title': 'geekShop - каталог',
        # 'categories': ProductCategory.objects.all()
        'categories': get_categories()
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
#     paginate_by = 3
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(category_id=self.kwargs['category_id'])
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductsListView, self).get_context_data(**kwargs)
#         context['title'] = 'geekShop - каталог'
#         context['categories'] = get_object_or_404(ProductCategory, category_id=self.kwargs['category_id'])
#         return context


