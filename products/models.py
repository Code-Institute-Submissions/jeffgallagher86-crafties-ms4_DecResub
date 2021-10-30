from django.db import models


class BreweryCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Brewery Category'

    name = models.CharField(max_length=254)
    brewery_description = models.TextField(blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class StyleCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Style Category'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CountryCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Country Category'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    brewery = models.ForeignKey(
        'BreweryCategory', null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey(
        'StyleCategory', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        'CountryCategory', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True)
    abv = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
