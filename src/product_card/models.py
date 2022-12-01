from django.db import models
from datetime import date


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    price = models.DecimalField(("price"), max_digits=5, decimal_places=2)
    authors = models.ForeignKey('reference_book.Author', on_delete=models.PROTECT, related_name='book')
    series = models.ForeignKey('reference_book.Seria', on_delete=models.PROTECT, related_name='book')
    genre = models.ForeignKey('reference_book.Genre', on_delete=models.PROTECT, related_name='book')
    published = models.DateField(null=True)
    pages = models.IntegerField()
    binding = models.CharField(max_length=40)
    book_format = models.CharField(max_length=40, blank=True, null=True, default='')
    ISBN = models.CharField(max_length=40)
    weight = models.IntegerField()
    allowed_age = models.IntegerField(blank=True, null=True, default=0)
    publisher = models.ForeignKey('reference_book.Publisher', on_delete=models.PROTECT, related_name='book')
    available = models.IntegerField()
    active = models.BooleanField(default='Yes')
    rating = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateField()
    updated = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name