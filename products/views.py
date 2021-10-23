from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, BreweryCategory, StyleCategory, CountryCategory


def all_products(request):
    """ View to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    breweries = None
    styles = None
    countries = None
    sort = None
    direction = None

    # Sorts products by price or a-z for each category

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'brewery':
                sortkey = 'brewery__name'
            elif sortkey == 'style':
                sortkey = 'style__name'
            elif sortkey == 'country':
                sortkey = 'country__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    # Filters products by brewery, style or country and search function

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_breweries': breweries,
        'current_styles': styles,
        'current_countries': countries,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
