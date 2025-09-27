from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Brand, Product, Category
from .serializers import BrandSerializer, ProductSerializer, CategorySerializer
from .filters import ProductFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser



# Product viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,   #  handles min_price, max_price, category, available
        filters.OrderingFilter,
        filters.SearchFilter   # keeping free-text search separate
    ]
    filterset_class = ProductFilter

    ordering_fields = ['price', 'created_at', 'name', 'stock']
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'category__name']



#Product category viewset
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# #Product brand viewset
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

