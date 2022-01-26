import uuid

from commons.choices import MaturityRating
from commons.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Movie(BaseModel):
    class MovieType(models.IntegerChoices):
        SEASONAL = 1, "Seasonal"
        SINGLE = 2, "Single"

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    identifier = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=MovieType.choices)
    flyer = models.ImageField(upload_to="flyers", blank=True, null=True)

    maturity_rating = models.PositiveSmallIntegerField(
        choices=MaturityRating.choices,
        verbose_name=_("maturity rating"),
        null=False,
        blank=False,
    )
    kid_profile = models.BooleanField(
        verbose_name=_("Kid's movie"),
        blank=True,
        null=False,
        default=False,
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    @property
    def rating_display(self):
        return self.get_maturity_rating_display()


class Video(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="movies")
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="videos"
    )

    def __str__(self) -> str:
        return self.title or self.movie.title
