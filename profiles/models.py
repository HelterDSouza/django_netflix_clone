import uuid

from commons.choices import MaturityRating
from commons.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()


class Profile(BaseModel):
    identifier = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=255)
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profiles",
    )
    maturity_rating = models.PositiveSmallIntegerField(
        choices=MaturityRating.choices,
        verbose_name=_("maturity rating"),
        null=False,
        blank=False,
        help_text=_("Only show title rated with"),
    )
    kid_profile = models.BooleanField(
        verbose_name=_("kids profile"),
        blank=True,
        null=False,
        default=False,
        help_text=_("Display the Netflix Kids experience with titles just for kids"),
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    @property
    def rating_display(self) -> str:
        return self.get_maturity_rating_display()
