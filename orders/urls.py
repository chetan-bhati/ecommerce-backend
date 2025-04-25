from django.urls import path
from orders.views import OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:id>/', OrderDetailView.as_view(), name='order-detail'),
]
