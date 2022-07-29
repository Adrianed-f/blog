from django.conf import settings
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
        blank=True,
        null=True
    )

    country = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    house = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
# Create your models here.
