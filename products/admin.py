from django.contrib import admin
from .models import Product, BreweryCategory, StyleCategory, CountryCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brewery',
        'style',
        'country',
        'price',
        'size',
        'abv',
        'image',
    )

    ordering = ('sku',)


class BreweryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class StyleCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CountryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(BreweryCategory, BreweryCategoryAdmin)
admin.site.register(StyleCategory, StyleCategoryAdmin)
admin.site.register(CountryCategory, CountryCategoryAdmin)
