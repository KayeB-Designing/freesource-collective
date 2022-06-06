from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']