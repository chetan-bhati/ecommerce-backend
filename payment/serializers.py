from rest_framework import serializers
from payment.models import Payment
from orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'payment_method', 'payment_status', 'payment_date']
        read_only_fields = ['id', 'payment_status', 'payment_date']
