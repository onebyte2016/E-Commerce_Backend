from django.db import migrations


def fix_image_urls(apps, schema_editor):
    ProductImage = apps.get_model("catalog", "ProductImage")

    for img in ProductImage.objects.all():
        if img.image and "e-commerce-backend-hvtu.onrender.com" in str(img.image):
            fixed_url = str(img.image).replace(
                "https://e-commerce-backend-hvtu.onrender.com/https%3A/",
                "https://"
            )
            img.image = fixed_url
            img.save(update_fields=["image"])


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0015_remove_productimage_cloudinary_url_and_more"),  # update this
    ]

    operations = [
        migrations.RunPython(fix_image_urls),
    ]
