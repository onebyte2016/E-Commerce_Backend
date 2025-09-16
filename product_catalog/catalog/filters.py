import django_filters
from django.db.models import Q
from .models import Product


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
        qs = queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))
        print("DEBUG SQL:", qs.query)
        return qs
