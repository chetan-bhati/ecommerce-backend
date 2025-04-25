from django.contrib import admin
from orders.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Removes the empty extra forms

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)

admin.site.register(Order, OrderAdmin)
