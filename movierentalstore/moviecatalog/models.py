from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class MovieGenre(models.Model):
    movie_genre = models.CharField(max_length=50, unique=True, help_text='Enter a movie genre (e.g. Action)')

    def __str__(self):
        return self.movie_genre


class Movie(models.Model):
    genre = models.ForeignKey(MovieGenre, on_delete=models.RESTRICT)
    movie_name = models.CharField(max_length=225)
    movie_rating = models.CharField(max_length=10, null=True)
    launch_date = models.DateTimeField('date launched', null=True)
    price = models.IntegerField(default=0)

    KE_SHILLINGS = 'Kshs'

    CURRENCY_CHOICES = [(KE_SHILLINGS, 'Kenya Shillings')]
    
    sale_currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default=KE_SHILLINGS)
    sku = models.CharField(max_length=5, default=0000, null=False)

    def __str__(self):
        return f'{self.genre} {self.movie_name} {self.sale_currency} {self.price}'
