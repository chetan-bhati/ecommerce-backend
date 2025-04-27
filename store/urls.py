from django.urls import path, include
from store.views import CategoryView,ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductView, basename='product')
router.register(r'categories', CategoryView, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
