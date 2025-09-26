import cloudinary
import cloudinary.uploader
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



# class ProductImageSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = ProductImage
#         fields = ["id", "image"]

#     def get_image(self, obj):
#         # If image exists, return the full Cloudinary URL
#         return obj.image.url if obj.image else None

# class CloudinaryImageField(serializers.ImageField):
#     def to_representation(self, value):
#         if not value:
#             return None
#         url = getattr(value, "url", value)
#         return str(url)  # ensure Cloudinary absolute URL, no SITE_URL prefix
# class ProductImageSerializer(serializers.ModelSerializer):
#     image = CloudinaryImageField(read_only=True)

#     class Meta:
#         model = ProductImage
#         fields = ["id", "image"]


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






# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ["id", "image"]

#     def create(self, validated_data):
#         image_file = validated_data.get("image")

#         # Upload file to Cloudinary
#         upload_result = cloudinary.uploader.upload(image_file, folder="product_images")

#         # Save the Cloudinary URL into the model
#         validated_data["image"] = upload_result["secure_url"]
#         return super().create(validated_data)


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



# class ProductCreateSerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         child=serializers.ImageField(), write_only=True, required=False
#     )
#     category_id = serializers.PrimaryKeyRelatedField(
#         source="category", queryset=Category.objects.all(), write_only=True
#     )
#     brand = serializers.PrimaryKeyRelatedField(
#         queryset=Brand.objects.all(), write_only=True
#     )

#     class Meta:
#         model = Product
#         fields = [
#             "id", "name", "slug", "description", "initial_price", "price",
#             "stock", "available", "category_id", "brand", "images"
#         ]
#         read_only_fields = ["id", "slug"]

#     def create(self, validated_data):
#         images = validated_data.pop("images", [])
#         product = super().create(validated_data)

#         for image in images:
#             # Upload to Cloudinary
#             result = cloudinary.uploader.upload(image, folder="product_images")

#             # Save secure URL in DB
#             ProductImage.objects.create(
#                 product=product,
#                 image=result["secure_url"]
#             )

#         return product

# class ProductCreateSerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         child=serializers.ImageField(), write_only=True, required=False
#     )
#     category_id = serializers.PrimaryKeyRelatedField(
#         source="category", queryset=Category.objects.all(), write_only=True
#     )
#     brand = serializers.PrimaryKeyRelatedField(
#         queryset=Brand.objects.all(), write_only=True
#     )

#     class Meta:
#         model = Product
#         fields = [
#             "id", "name", "slug", "description", "initial_price", "price",
#             "stock", "available", "category_id", "brand", "images"
#         ]
#         read_only_fields = ["id", "slug"]

#     def create(self, validated_data):
#         images = validated_data.pop("images", [])
#         product = super().create(validated_data)

#         for image in images:
#             # Just save the file — ProductImage.save() will handle Cloudinary upload
#             ProductImage.objects.create(product=product, image=image)

#         return product

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
