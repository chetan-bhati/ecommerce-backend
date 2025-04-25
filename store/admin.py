from django.contrib import admin
from store.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('-created_at',)

admin.site.register(Product, ProductAdmin)
