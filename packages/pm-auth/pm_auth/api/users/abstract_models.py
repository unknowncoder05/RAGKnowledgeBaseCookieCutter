from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from pm_utils.api.utils.models import BaseModel
from .roles import UserRoles
from .auth.external_token.providers import ExternalAuthenticationTokenProviders


class AbstractPMUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class AbstractPMUser(BaseModel, AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    terms_and_conditions = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    preferred_provider = models.CharField(
        choices=ExternalAuthenticationTokenProviders.choices,
        null=False,
        default=ExternalAuthenticationTokenProviders.SMS,
        max_length=10,
        blank=False
    )
    preferred_language_code = models.CharField(default='es', max_length=5)
    role = models.CharField(choices=UserRoles.choices, max_length=5, blank=True, null=True)
    public = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to='user/%Y/%m/%d/')
    identity_number = models.CharField(max_length=20, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    recommendation = models.TextField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)

    # GitHub OAuth fields
    github_id = models.CharField(max_length=50, null=True, blank=True, unique=True)
    github_username = models.CharField(max_length=100, null=True, blank=True)
    github_access_token = models.TextField(null=True, blank=True)
    github_token_expires_at = models.DateTimeField(null=True, blank=True)

    objects = AbstractPMUserManager()

    class Meta:
        abstract = True
        ordering = ['email']

    def __str__(self):
        return self.email if self.email else '' 

    def save(self, *args, **kwargs):
        if self.is_verified:
            self.verified_at = now()
        else:
            self.verified_at = None
        return super().save(*args, **kwargs)

    @property
    def public_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} {self.role}'.strip()

    def get_owner(self):
        return self

    def is_public(self):
        return self.public

    def is_app_superuser(self):
        return self.role == UserRoles.SUPERUSER.value

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
