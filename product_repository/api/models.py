import uuid

from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to=settings.RAW_LOGOS_URL)
    rotate_duration = models.FloatField(null=True, blank=True)
    modified = models.BooleanField(default=False)