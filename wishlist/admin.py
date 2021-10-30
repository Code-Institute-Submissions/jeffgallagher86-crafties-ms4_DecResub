from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist_user',
        'product',
    )


admin.site.register(Wishlist, WishlistAdmin)