from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class LinkedEntry(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(max_length=500)

    class Meta:
        abstract = True

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"


class ProjectEntry(LinkedEntry):
    description = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name_plural = "project entries"


class ProjectEntryWebHook(LinkedEntry):
    class Meta:
        verbose_name_plural = "project entry web hook"
