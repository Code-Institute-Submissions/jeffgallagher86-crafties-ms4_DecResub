from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    wishlist_user = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE,
        null=True, blank=True, related_name='wishlist')
    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE,
        null=True, blank=True, related_name='wishlist_products')

    def __str__(self):
        return f"{self.wishlist_user}'s Wishlist"
