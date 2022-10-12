from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_lehgth=30)
    surname = models.CharField(max_lehgth=30)

class Seria(models.Model):
    name = models.CharField(max_lehgth=120)
    description = models.TextField(
        blank=True,
        null=True
    )

class Genre(models.Model):
    name = models.CharField(max_lehgth=120)
    description = models.TextField(
        blank=True,
        null=True
    )

class Publisher(models.Model):
    name = models.CharField(max_lehgth=120)
    description = models.TextField(
        blank=True,
        null=True
    )