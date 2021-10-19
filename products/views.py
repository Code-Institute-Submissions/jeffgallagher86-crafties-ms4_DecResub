from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, BreweryCategory, StyleCategory, CountryCategory

# Create your views here.


def all_products(request):
    """ View to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    breweries = None
    styles = None
    countries = None

    if request.GET:
        if 'brewery' in request.GET:
            breweries = request.GET['brewery'].split(',')
            products = products.filter(brewery__name__in=breweries)
            breweries = BreweryCategory.objects.filter(name__in=breweries)

        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            products = products.filter(style__name__in=styles)
            styles = StyleCategory.objects.filter(name__in=styles)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            countries = CountryCategory.objects.filter(name__in=countries)
    
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_breweries': breweries,
        'current_styles': styles,
        'current_counries': countries,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
