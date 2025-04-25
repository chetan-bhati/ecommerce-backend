from django.urls import path
from review.views import ReviewCreateView, ReviewListView, ReviewDeleteView, ReviewUpdateView

urlpatterns = [
    path('add/', ReviewCreateView.as_view(), name='add-review'),
    path('product/<int:product_id>/', ReviewListView.as_view(), name='reviews-for-product'),
    path('delete/<int:id>/', ReviewDeleteView.as_view(), name='delete-review'),
    path('update/<int:id>/', ReviewUpdateView.as_view(), name='update-review'),
]
