from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.choises import RoleChoises


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    fullname = models.CharField(_("full name"), max_length=150, blank=True)
    phone_number = models.CharField(max_length=9, unique=True)
    role = models.CharField(max_length=123, choices=RoleChoises.choices)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return f"{self.fullname}"


class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_id = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"

    def __str__(self):
        return f"Telegram user {self.chat_id}"


class TelegramUserState(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    logs = models.JSONField(default=dict())

    class Meta:
        verbose_name= "Telegram State"
        verbose_name_plural = "Telegram States"

    def __str__(self):
        return f"Telegram State {self.chat_id}"
