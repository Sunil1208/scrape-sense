import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(
        verbose_name="User ID", default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True, verbose_name="Email ID")
    first_name = models.CharField(verbose_name="First Name", max_length=60)
    last_name = models.CharField(verbose_name="Last Name", max_length=60)
    username = models.CharField(verbose_name="Username", max_length=60, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    objects = CustomUserManager()

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.username
