from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist_toggle/<int:product_id>',
         views.wishlist_toggle, name='wishlist_toggle'),
]
