from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    score = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"score : {self.score} from user : {self.user.username} / {self.month}"
