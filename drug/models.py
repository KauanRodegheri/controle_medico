from django.db import models
from django.contrib.auth.models import User

class Drug(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Hours(models.Model):
    hours = models.TimeField()
    drugs = models.ManyToManyField(Drug, related_name='drugs')

    def __str__(self):
        return str(self.hours)
    
