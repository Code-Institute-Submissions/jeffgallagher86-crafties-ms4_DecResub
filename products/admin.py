from django.contrib import admin
from .models import Product, BreweryCategory, StyleCategory, CountryCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(BreweryCategory)
admin.site.register(StyleCategory)
admin.site.register(CountryCategory)
