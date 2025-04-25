from rest_framework import serializers
from orders.models import Order, OrderItem
from cart.serializers import CartItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = CartItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'updated_at', 'items']
        read_only_fields = ['user', 'created_at', 'updated_at', 'total_price']
