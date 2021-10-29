from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    wishlist_user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE,
                                      null=False, blank=False, related_name='wishlist')
    products = models.ManyToManyField('products.Product',
                                      related_name='wishlist_products')

    def __str__(self):
        return f"{self.wishlist_user}'s Wishlist"
