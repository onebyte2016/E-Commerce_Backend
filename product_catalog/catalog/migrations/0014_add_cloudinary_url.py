from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0013_alter_productimage_cloudinary_url"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE catalog_productimage
                ADD COLUMN cloudinary_url TEXT;
            """,
            reverse_sql="""
                ALTER TABLE catalog_productimage
                DROP COLUMN cloudinary_url;
            """,
        ),
    ]
