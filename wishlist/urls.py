from django.urls import path
from wishlist.views import WishlistCreateView, WishlistDeleteView, WishlistListView

urlpatterns = [
    path('add/', WishlistCreateView.as_view(), name='add-to-wishlist'),
    path('remove/<int:id>/', WishlistDeleteView.as_view(), name='remove-from-wishlist'),
    path('', WishlistListView.as_view(), name='wishlist-list'),
]
