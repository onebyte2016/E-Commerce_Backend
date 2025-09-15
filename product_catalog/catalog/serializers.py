from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id','name','slug','description','price','stock','available','image',
            'created_at','updated_at','category','category_id'
        ]
        read_only_fields = ['id','slug','created_at','updated_at']
