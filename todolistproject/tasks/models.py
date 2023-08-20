from django.db import models
from datetime import datetime


class Task(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=250, blank=False)
    is_done = models.BooleanField(default=False, blank=False)
    creation_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return f"Name: {self.name} / Description: {self.description} / Date: {self.creation_date}"
