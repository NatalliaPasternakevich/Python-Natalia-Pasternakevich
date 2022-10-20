from django import forms
from django.core.exceptions import ValidationError

from . import models

def name_validator(value: str):
    if value.startswith(''):
        raise ValidationError('You have forgotten about Fred!')
    return value

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'surname']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')
