from django.urls import path
from store.views import CategoryListView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
