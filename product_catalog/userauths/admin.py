from django.contrib import admin
from .models import CustomUser

# Register your models here.
# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_active")