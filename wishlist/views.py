from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Product, Wishlist


@login_required
def wishlist(request):
    """ A view to display the users wishlist """

    profile = get_object_or_404(UserProfile, user=request.user)
    wishlists = Wishlist.objects.filter(wishlist_user=profile)

    template = 'wishlist/wishlist.html'

    context = {
        'profile': profile,
        'wishlists': wishlists,
    }

    return render(request, template, context)


@login_required
def wishlist_toggle(request, product_id):
    """ A view to add and remove product to and from wishlist """

    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.filter(wishlist_user=profile, product=product)

    if wishlist:
        wishlist.delete()
        messages.info(
            request,
            f'{product.name} has been removed from your wishlist!')
        return redirect('/products/' + str(product.id) + '/')
    else:
        new_wishlist = Wishlist()
        new_wishlist.wishlist_user = profile
        new_wishlist.product = product
        new_wishlist.save()
        messages.success(request, f'{product.name} added to wishlist!')
        return redirect('/products/' + str(product.id) + '/')
