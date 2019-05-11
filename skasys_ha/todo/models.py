from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=160)
    date = models.DateField()
    progress = models.IntegerField()
