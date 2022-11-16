from django.contrib import admin
from . import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'authors')

admin.site.register(models.Book, BookAdmin)