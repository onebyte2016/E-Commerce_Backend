from rest_framework import serializers
from .models import Brand, Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )
    images = ProductImageSerializer(many=True, read_only=True)  # nested images

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "price", "stock", "available",
            "created_at", "updated_at", "category", "category_id", "images"
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]

class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "price", "stock",
            "available", "category_id", "images"
        ]

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        product = super().create(validated_data)
        for image in images:
            ProductImage.objects.create(product=product, image=image)
        return product
