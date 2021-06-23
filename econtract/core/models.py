from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_common.db_fields import JSONField
app_name = "core"


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = f"{self.model.USERNAME_FIELD}__exact"
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_staffuser(
            username=username,
            email=email,
            password=password,
        )
        user.email = email
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.role = "admin"
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, blank=True, db_index=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username


class Base(models.Model):
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)
    created_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_created_related",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_updated_related",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Contract(Base):
    TYPE = (
        ("bilateral", "bilateral"),
        ("multi_party", "multi_party"),
    )
    STATUS = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected")
    )
    upload = models.FileField(upload_to = 'upload/')
    type = models.CharField(max_length=128, choices=TYPE, default="bilateral")
    other_party_user = models.ManyToManyField(User, related_name="recieved_contract")
    reviewer_user =  models.ManyToManyField(User, related_name="contract_reviewer")
    user_approved = models.ManyToManyField(User, related_name="approved_contract",blank=True)
    user_reviewed = models.ManyToManyField(User, related_name="reviewed_contract",blank=True)
    status = models.CharField(max_length=128, choices=STATUS, default="pending")
    contract_expiry_date = models.DateField(blank=True, null=True)
    contract_update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.created_by.email
