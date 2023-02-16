from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class TypeWork(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    time = models.PositiveIntegerField(default=0)
    type_work = models.ManyToManyField(TypeWork, blank=True)
    is_finished = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title
