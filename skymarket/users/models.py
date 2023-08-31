from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class UserRoles(models.TextChoices):
        ADMIN = "admin", _("Admin")
        USER = "user", _("User")       


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices)
    image = models.ImageField(upload_to="userpics/", blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_staff(self):
        return self.role == UserRoles.ADMIN

    def has_perm(self, perm, obj=None):
        return self.role == UserRoles.ADMIN

    def has_module_perms(self, app_label):
        return self.role == UserRoles.ADMIN

    objects = UserManager()