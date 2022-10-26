from django.contrib import admin
from . import models

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


class SeriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')




admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Seria, SeriaAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publisher, PublisherAdmin)