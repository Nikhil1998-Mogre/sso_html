from django.contrib.auth.models import  BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    # use_in_migrations to True ensures that your custom manager is used instead of default manager
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        extra_fields.setdefault('email', '') # set email to an empty string if not present
        extra_fields.setdefault('password', 'password123') # set password to a default value
        extra_fields['email'] = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)
