from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email





# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from .managers import CustomUserManager
# # Create your models here.

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(unique=True, max_length=100,null=True, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
