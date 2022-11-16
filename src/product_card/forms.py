from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'name',
            'cover',
            'price',
            'authors',
            'series',
            'genre',
            'published',
            'pages',
            'binding',
            'book_format',
            'ISBN',
            'weight',
            'allowed_age',
            'publisher',
            'available',
            'active',
            'rating',
            'created',
            'updated',
            ]