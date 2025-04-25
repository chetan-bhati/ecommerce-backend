from rest_framework import generics, permissions
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer
from cart.models import Cart

class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        order = serializer.save(user=self.request.user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, cart_item=item, quantity=item.quantity)
        order.calculate_total_price()
        cart.items.all().delete()  # Clear cart after order
        return order


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
