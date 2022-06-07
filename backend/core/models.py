from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProjectEntry(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "project entries"
