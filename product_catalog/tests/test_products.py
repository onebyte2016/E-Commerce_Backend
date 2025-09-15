import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from catalog.models import Category, Product


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def category():
    return Category.objects.create(name='Electronics')


@pytest.fixture
def products(category):
    p1 = Product.objects.create(
        name='Phone A',
        description='Nice phone',
        price=199.99,
        stock=10,
        category=category
    )
    p2 = Product.objects.create(
        name='Phone B',
        description='Better phone',
        price=399.99,
        stock=5,
        category=category
    )
    return [p1, p2]


@pytest.mark.django_db
def test_list_products(api_client, products):
    url = reverse('product-list')
    resp = api_client.get(url)
    assert resp.status_code == 200
    # Using default PageNumberPagination; response has 'count' and 'results'
    assert resp.data['count'] == 2


@pytest.mark.django_db
def test_filter_min_price(api_client, products):
    url = reverse('product-list') + '?min_price=300'
    resp = api_client.get(url)
    assert resp.status_code == 200
    assert resp.data['count'] == 1
    assert resp.data['results'][0]['name'] == 'Phone B'


@pytest.mark.django_db
def test_ordering_by_price(api_client, products):
    url = reverse('product-list') + '?ordering=price'
    resp = api_client.get(url)
    assert resp.status_code == 200
    # DRF serializes Decimal as string in JSON; convert to float for comparison
    prices = [float(r['price']) for r in resp.data['results']]
    assert prices == sorted(prices)


@pytest.mark.django_db
def test_pagination(api_client, category):
    # create 15 products to test pagination (PAGE_SIZE default = 12)
    for i in range(15):
        Product.objects.create(name=f'P{i}', description='x', price=10 + i, stock=1, category=category)
    url = reverse('product-list')
    resp = api_client.get(url)
    assert resp.status_code == 200
    assert resp.data['count'] == 15
    # ensure pagination metadata exists and page size is respected
    assert 'next' in resp.data and 'previous' in resp.data
    assert len(resp.data['results']) <= 12
