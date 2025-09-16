from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter
from rest_framework.filters import OrderingFilter, SearchFilter



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,   #  handles min_price, max_price, category, available
        filters.OrderingFilter,
        filters.SearchFilter   # keep free-text search separate
    ]
    filterset_class = ProductFilter

    ordering_fields = ['price', 'created_at', 'name', 'stock']
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'category__name']
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     #  Enable filtering, ordering, searching
#     filter_backends = [DjangoFilterBackend, OrderingFilter]

#     filterset_class = ProductFilter
#     ordering_fields = ['price', 'created_at', 'name', 'stock']
#     ordering = ['-created_at']  # default ordering
#     search_fields = ['name', 'description', 'category__name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

