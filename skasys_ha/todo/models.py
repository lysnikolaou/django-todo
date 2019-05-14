from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=160)
    deadline = models.DateField()
    progress = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
