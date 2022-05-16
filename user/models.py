from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = 'male', _('male')
        FEMALE = 'female', _('female')
        OTHERS = 'others', _('others')

    class Status(models.TextChoices):
        ACTIVE = 'active', _('active')
        ARCHIVED = 'archived', _('archived')
        DELETED = 'deleted', _('deleted')


    verified = models.BooleanField(default=False)
    profile_pic_url = models.TextField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    user_status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(_('email address'))
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['verified', 'gender', 'email', 'user_status', 'is_superuser', 'is_staff', 'is_active']
    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-date_joined']
        default_permissions = ('add', 'change', 'view', )

    def __str__(self):
        return self.username