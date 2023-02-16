from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ItemSport(models.Model):
    title = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=0)
    repeat_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Sport(models.Model):
    title = models.CharField(max_length=255, blank=True)
    members = models.ManyToManyField(User, related_name='sports', blank=True)
    items = models.ManyToManyField(ItemSport, related_name='sports_items')

    def __str__(self) -> str:
        return self.title
