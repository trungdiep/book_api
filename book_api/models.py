from django.db import models
from django.db.models.fields import SlugField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.CharField(max_length=5)
    review = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title

