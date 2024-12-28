from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from movies.models import Movie


class Review(models.Model):
    moview = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    starts = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação nao pode ser inferior a 0'),
            MaxValueValidator(5, 'Avalização não pode ser maior que 5'),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.moview


