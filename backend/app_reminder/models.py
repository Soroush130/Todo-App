from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title



