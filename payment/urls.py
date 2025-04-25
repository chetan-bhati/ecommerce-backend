from django.urls import path
from payment.views import PaymentCreateView, PaymentDetailView

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='create-payment'),
    path('<int:id>/', PaymentDetailView.as_view(), name='payment-detail'),
]
