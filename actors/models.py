from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil')
)


class Actor(models.Model):
    name = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        choices=NATIONALITY_CHOICES,
        max_length=100,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
    
