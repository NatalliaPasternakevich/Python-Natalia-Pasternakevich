from django import forms
from . import models

class HomePageForm(forms.ModelForm):
    class Meta:
        model = models.HomePage
        fields = []