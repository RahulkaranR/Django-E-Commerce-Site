from django.shortcuts import render, get_object_or_404

from .models import Category, product


def all_products(request):
    Products = product.objects.all()
    return render(request, 'store/home.html', {"Products":Products})

def product_detail(request, slug):
    Products = get_object_or_404(product, slug=slug, in_stock=True)
    return render(request, 'store/products/details.html', {'Products':Products})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    Products = product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category, 'Products':Products})










