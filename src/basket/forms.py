from django import forms
from . import models

class BookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ('contact_phone', 'address',)

    