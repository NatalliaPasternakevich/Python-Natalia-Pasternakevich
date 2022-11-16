from django.contrib import admin
from . import models
# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.HomePage, HomePageAdmin)
# Register your models here.

