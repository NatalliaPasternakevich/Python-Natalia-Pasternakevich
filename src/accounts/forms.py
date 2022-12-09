from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . import models 

# Register your models here.

User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['phone', 'country', 'city','zip_code','address1', 'address2', 'information']