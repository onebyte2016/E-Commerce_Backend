from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_productimage_cloudinary_url'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE catalog_productimage
                ALTER COLUMN cloudinary_url TYPE TEXT;
            """,
            reverse_sql="""
                ALTER TABLE catalog_productimage
                ALTER COLUMN cloudinary_url TYPE varchar(100);
            """,
        ),
        migrations.RunSQL(
            sql="""
                ALTER TABLE catalog_productimage
                ALTER COLUMN image TYPE TEXT;
            """,
            reverse_sql="""
                ALTER TABLE catalog_productimage
                ALTER COLUMN image TYPE varchar(100);
            """,
        ),
    ]
