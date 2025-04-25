from django.db import models
from django.conf import settings
from store.models import Product

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 rating
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"

    class Meta:
        unique_together = ('user', 'product')  # Prevent a user from reviewing the same product multiple times
