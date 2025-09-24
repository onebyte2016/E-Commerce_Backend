from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'brand', BrandViewSet, basename='brand')

urlpatterns = router.urls
