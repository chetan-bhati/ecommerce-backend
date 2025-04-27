from django.contrib import admin
from wishlist.models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__email', 'product__name')
    list_filter = ('product',)
