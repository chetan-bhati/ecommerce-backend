from django.contrib import admin
from review.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_at',)

admin.site.register(Review, ReviewAdmin)
