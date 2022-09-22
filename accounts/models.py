from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    # Override fields
    email = models.EmailField(_("Email"), max_length=225, unique=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True
    )

    # Database constants
    ROLE_CHOICES = (
        (str(1), _("CEO"), ), 
        (str(2), _("Admin"), ), 
        (str(3), _("Seller"), ), 
        (str(4), _("The User"), ), 
    )

    # New fields
    avatar = models.ImageField(_("Avatar"), upload_to="accounts/", blank=True)
    bio = models.TextField(_("Bio"), null=True, blank=True)
    role = models.CharField(_("Role"), max_length=1, choices=ROLE_CHOICES, default=str(4))

    class Meta:
        """In this class, We can edit or update the model (or database table) settings."""

        # Translation and names
        verbose_name = _("User")
        verbose_name_plural = _("users")

    def __unicode__(self) -> str:
        return self.username
    
    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str: 
        return self.username
