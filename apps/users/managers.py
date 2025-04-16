from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valid email")

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        if not username:
            raise ValueError("Username is required")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if not password:
            raise ValueError("Password is required")

        if not email:
            raise ValueError("Email is required")
        else:
            email = self.normalize_email(email)  # Normalize email
            self.email_validator(email)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Email is required")

        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            **extra_fields
        )

        user.save(using=self._db)
        return user
