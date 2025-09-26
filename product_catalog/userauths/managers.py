from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,   # ✅ include username
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, username, password, **extra_fields)







# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Users must have an email address")

#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)   # ✅ hashes the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         return self.create_user(email, username, password, **extra_fields)
