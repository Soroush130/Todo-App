from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Water(models.Model):
    date = models.DateField()
    count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.date} from {self.user.username}"
