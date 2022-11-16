from django.db import models
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class HomePage(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name 

    def __repr__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse_lazy('reference:genre-detail', kwargs={'pk': self.pk})

