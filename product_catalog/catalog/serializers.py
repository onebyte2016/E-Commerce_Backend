import cloudinary
import cloudinary.uploader
from rest_framework import serializers
from .models import Brand, Category, Product, ProductImage


#Serializers for product category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']

#Serializers for product brand
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'description', 'created_at']

#Serializers for product image
class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ["id", "image"]

    def get_image(self, obj):
        if obj.image:
            # Return raw Cloudinary URL instead of Django's .url
            return str(obj.image)
        return None

#serializers for product
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )
    images = ProductImageSerializer(many=True, read_only=True)  # nested images

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "initial_price", "price", "stock", 
            "available", "created_at", "updated_at", "category", "brand", 
            "category_id", "images"
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]

#Serializer for creating product
class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    product_images = ProductImageSerializer(source="productimage_set", many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "initial_price", "price",
            "stock", "available", "category_id", "brand", "images", "product_images"
        ]
        read_only_fields = ["id", "slug"]

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        product = super().create(validated_data)

        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return product
