from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email_or_phone, password=None, **extra_fields):
        if not email_or_phone:
            raise ValueError("Users must have an email_or_phone or phone number")
        email_or_phone = self.normalize_email(email_or_phone) if '@' in email_or_phone else email_or_phone
        user = self.model(
            email_or_phone=email_or_phone, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_or_phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email_or_phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email_or_phone = models.CharField(
        verbose_name='email or phone number',
        max_length=255,
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email_or_phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email_or_phone


class OTPCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email_or_phone = models.CharField(
        verbose_name='email or phone number',
        max_length=255,
        unique=True,
    )
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_or_phone
