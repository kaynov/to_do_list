from django.db import models
from datetime import datetime


class Tasks(models.Model):

    name = models.CharField(
        max_length=100, help_text="Список задач",
    )
    start_time = models.DateTimeField(
        auto_now_add=True, help_text="Время создания",
    )
    status = models.BooleanField(
        default=False, help_text="Статус",
    )
    end_time = models.DateTimeField(
        blank=True, null=True, help_text="Время завершения",
    )
