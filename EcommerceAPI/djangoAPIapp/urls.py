from django.urls import path
from .views import ListBook, ListCategory, ListProduct, DetailBook, DetailCategory, DetailProduct



urlpatterns = [
    path('category/', ListCategory.as_view(), name='categories'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='Specific_category'),
    path('books/', ListBook.as_view(), name='Books'),
    path('book/<int:pk>/', DetailBook.as_view(), name='Specific_book'),
    path('product/', ListProduct.as_view(), name='Products'),
    path('Product/<int:pk>/', DetailProduct.as_view(), name='Specific_product'),
]