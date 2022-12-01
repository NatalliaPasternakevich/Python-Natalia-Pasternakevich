from django.contrib import admin
from . import models
# Register your models here.

class BasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')

class GoodsInBasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'order', 'quantity', 'price', 'created', 'updated')

admin.site.register(models.Basket, BasketAdmin)
admin.site.register(models.GoodsInBasket, GoodsInBasketAdmin)