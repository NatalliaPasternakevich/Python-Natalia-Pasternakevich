from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Autor)
admin.site.register(models.Seria)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)