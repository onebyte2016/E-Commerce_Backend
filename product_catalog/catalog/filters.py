import django_filters
from .models import Product
from . import models

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Product
        fields = ['category','available','min_price','max_price','search']

    def filter_search(self, queryset, name, value):
        # Simple icontains search across name and description:
        return queryset.filter(models.Q(name__icontains=value) | models.Q(description__icontains=value))
