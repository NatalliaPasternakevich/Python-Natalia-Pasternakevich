from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'surname']


class SeriaForm(forms.ModelForm):
    class Meta:
        model = models.Seria
        fields = ['name', 'description']


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name', 'description']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = ['name', 'description']   
