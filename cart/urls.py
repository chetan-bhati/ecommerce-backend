from django.urls import path
from cart.views import CartDetailView, CartItemAddUpdateView, CartItemDeleteView

urlpatterns = [
    path('', CartDetailView.as_view(), name='view-cart'),
    path('items/', CartItemAddUpdateView.as_view(), name='add-update-cart-item'),
    path('items/<int:pk>/', CartItemDeleteView.as_view(), name='remove-cart-item'),
]
