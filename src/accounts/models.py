from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User_min_data = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User_min_data, on_delete=models.PROTECT, related_name='customer')
    phone = models.CharField(max_length=40)
    country = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    zip_code = models.CharField(max_length=40, blank=True, null=True)
    address1 = models.CharField(max_length=40, blank=True, null=True)
    address2 = models.CharField(max_length=40, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
  

    def __str__(self):
        return self.user.username