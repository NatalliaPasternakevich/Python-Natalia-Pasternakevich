from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + (self.surname)

    def get_absolute_url(self):
        return f'ref-autor/{self.pk}'

class Seria(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

class Genre(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

class Publisher(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 