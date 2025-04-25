from rest_framework import serializers
from review.models import Review
from store.models import Product

class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product', 'product_name', 'rating', 'review_text', 'created_at']
        read_only_fields = ['id', 'created_at']
