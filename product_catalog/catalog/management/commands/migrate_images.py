from django.core.management.base import BaseCommand
from cloudinary.uploader import upload
import cloudinary
from catalog.models import ProductImage  # adjust to your model
import os

class Command(BaseCommand):
    help = "Migrate local product images to Cloudinary"

    def handle(self, *args, **kwargs):
        # Ensure Cloudinary is configured
        cloudinary.config(
            cloud_name="dzlpsd12b",
            api_key="749879934386175",
            api_secret="gkETr_8MCaIvthuCoaFObA43jzg",
            secure=True
        )

        for product_image in ProductImage.objects.all():
            if not product_image.image:
                continue

            try:
                local_path = product_image.image.path
            except Exception:
                self.stdout.write(self.style.WARNING(f"Skipping {product_image.id}, no local path"))
                continue

            if os.path.exists(local_path):
                self.stdout.write(f"Uploading {local_path}...")
                result = upload(local_path, folder="product_images")
                product_image.image = result["secure_url"]
                product_image.save(update_fields=["image"])
                self.stdout.write(self.style.SUCCESS(f"Updated {product_image.id}"))
