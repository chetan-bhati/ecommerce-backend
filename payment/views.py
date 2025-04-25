from rest_framework import generics, permissions, serializers
from payment.models import Payment
from payment.serializers import PaymentSerializer
from orders.models import Order

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order')
        order = Order.objects.get(id=order_id, user=self.request.user)
        if order.status != 'pending':
            raise serializers.ValidationError("Order cannot be paid because it is not in 'pending' status.")
        
        payment_method = self.request.data.get('payment_method')
        amount = order.total_price

        # Here you would integrate with a real payment gateway (e.g., Stripe, PayPal).
        # For now, we'll simulate a successful payment:
        payment = serializer.save(order=order, amount=amount, payment_method=payment_method, payment_status='successful')

        order.status = 'paid'
        order.save()

        return payment


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
