from django.db import models


class MaturityRating(models.IntegerChoices):
    R01 = 1, "L"
    R10 = 2, "10"
    R12 = 3, "12"
    R14 = 4, "14"
    R16 = 5, "16"
    R18 = 6, "18"
