from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)
    
    def __str__(self):
        return self.name
