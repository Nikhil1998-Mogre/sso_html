from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
    # fields
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=('groups'),
    #     blank=True,
    #     help_text=(
    #         'The groups this user belongs to. A user will get all permissions '
    #         'granted to each of their groups.'
    #     ),
    #     related_name='customuser_set', # <--- add this
    #     related_query_name='user',
    # )
    
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=('user permissions'),
    #     blank=True,
    #     help_text=('Specific permissions for this user.'),
    #     related_name='customuser_set', # <--- add this
    #     related_query_name='user',
    # )



    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users',  # Choose a unique related_name
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_users',  # Choose a unique related_name
        related_query_name='custom_user',
    )


