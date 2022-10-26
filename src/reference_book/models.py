from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + (self.surname)

    def __repr__(self):
        return self.name 

    def get_absolute_url(self):
        # return f'ref-autor/{self.pk}' было так
        return reverse_lazy('reference_book:author-detail', kwargs={'pk': self.pk})

class Seria(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('reference:seria-detail', kwargs={'pk': self.pk})       

class Genre(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('reference:genre-detail', kwargs={'pk': self.pk})


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

    def __repr__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse_lazy('reference:publisher-detail', kwargs={'pk': self.pk})

    