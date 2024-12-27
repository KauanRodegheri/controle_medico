from django.db import models
from django.contrib.auth.models import User


class Exams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exams')
    file = models.FileField()
    day = models.DateField()

    class Meta:
        ordering = ['day']


