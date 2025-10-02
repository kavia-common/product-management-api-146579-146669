from django.urls import path
from .views import (
    health,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('health/', health, name='Health'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
