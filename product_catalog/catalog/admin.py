from django.contrib import admin
from catalog.models import Category, Product, ProductImage, Brand


# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)



class ProductImageInline(admin.TabularInline):  # or admin.StackedInline
    model = ProductImage
    extra = 1  # show 1 empty slot by default

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "available", "created_at")
    list_filter = ('available', 'category', 'brand', 'created_at')
    search_fields = ('name', 'price', 'description')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]

    # Pagination
    list_per_page = 8   # show 20 products per page
    list_max_show_all = 200  # if you click "Show all", max 200 products


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image")

