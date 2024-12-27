from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    day = models.DateTimeField(verbose_name='Data')
    specialist = models.CharField(max_length=100, verbose_name='Especialista')
    hospital = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.specialist} - {self.day}'

    class Meta:
        ordering = ['day']